from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Visualization, LastfmUserProfile, SiteUserProfile
from .adapters.lastfm import user as lastfmUser
from datetime import datetime
from .services.stackplot import create_dummy_streamgraph
from .services.store_image import save_matplotlib_figure

def index(request):
    visualizations = Visualization.objects.order_by('-created_at')[:20]
    return render(request, 'index.html', {'visualizations': visualizations})


def fetch_user_stats(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()

        # Save default username if the user is authenticated and checked the box
        if request.user.is_authenticated and request.POST.get('set_default_lastfm'):
            profile = request.user.siteuserprofile
            profile.default_lastfm_username = username
            profile.save()

        # Redirect to loading page
        return redirect('loading_user_stats', username=username)

    return redirect('index')


def loading_user_stats(request, username):
    # Fetch info from API
    info = lastfmUser.get_info(username)
    user_data = info["user"]

    avatar = user_data["image"][-1]["#text"] if user_data.get("image") else None  # largest img
    registered_ts = user_data["registered"].get("unixtime")

    # Save/Update profile
    LastfmUserProfile.objects.update_or_create(
        lastfm_username=username,
        defaults={
            "display_name": user_data.get("name"),
            "profile_url": user_data.get("url"),
            "avatar_url": avatar,
            "registered_date": datetime.fromtimestamp(int(registered_ts)) if registered_ts else None,
        }
    )

    return redirect("user_stats", username=username)


def user_stats(request, username):
    # Get profile from DB
    profile = get_object_or_404(LastfmUserProfile, lastfm_username=username)

    # Fetch data from Last.fm
    info = lastfmUser.get_info(username)
    artists = lastfmUser.get_top_artists(username, limit=5)
    albums = lastfmUser.get_top_albums(username, limit=5)
    tracks = lastfmUser.get_top_tracks(username, limit=10)
    recent = lastfmUser.get_recent_tracks(username, limit=10)

    context = {
        "profile": profile,
        "total_scrobbles": info["user"]["playcount"],
        "recent_tracks": recent["recenttracks"]["track"],
        "top_artists": artists["topartists"]["artist"],
        "top_albums": albums["topalbums"]["album"],
        "top_tracks": tracks["toptracks"]["track"],
    }

    return render(request, "user_stats.html", context)


def visualization_options(request, username):
    # On POST, send visualization options data to backend which creates an empty viz entry in the db and returns the id
    # Then render loading page with the id
    return render(request, 'visualization_options.html', {'username': username})

def demo_visualization(request):
    # Make the dummy streamgraph
    fig = create_dummy_streamgraph()
    # Get a temporary hardcoded Lastfm_User_Profile object to use for required fields
    lastfmProfile = LastfmUserProfile.objects.get(lastfm_username='shazamuel89')
    # Create the empty db entry
    viz = Visualization.objects.create(
        lastfm_user=lastfmProfile,
        visualization_type='demo_streamgraph'
    )
    # Save the figure to the db
    save_matplotlib_figure(fig, viz)
    # Render the result page with the dummy visualization
    return render(request, "visualization_result.html", {"visualization": viz})


def loading_visualization(request, visualization_id):
    # Render page
    # Fetch needed data from lastfm
    # Create visualization
    # Upon finishing, redirect to visualization_result page
    return render(request, 'loading_visualization.html', {'id': visualization_id})


def visualization_result(request, visualization_id):
    return render(request, 'visualization_result.html', {'id': visualization_id})


@login_required
def account(request):
    site_profile = request.user.siteuserprofile
    default_username = site_profile.default_lastfm_username

    lastfm_profile = None
    if default_username:
        lastfm_profile = LastfmUserProfile.objects.filter(lastfm_username=default_username).first()

    context = {
        'default_username': default_username,
        'lastfm_profile': lastfm_profile,
        'previous_visualizations': request.user.saved_visualizations.all(),
        'favorite_visualizations': request.user.favorite_visualizations.all(),
    }

    return render(request, 'account.html', context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            # CREATE the SiteUserProfile for this user
            SiteUserProfile.objects.create(user=new_user)

            login(request, new_user)
            return redirect('account')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def about(request):
    return render(request, 'about.html')