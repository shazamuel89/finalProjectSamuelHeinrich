from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm, VisualizationOptionsForm
from .models import Visualization, LastfmUserProfile, SiteUserProfile
from .adapters.lastfm import user as lastfmUser
from datetime import datetime
from .services.stackplot import create_data_fed_streamgraph
from .services.store_graph import save_plotly_figure
from .services.get_visualization_data import get_lastfm_data

def index(request):
    visualizations = Visualization.objects.order_by('-created_at')[:20]
    return render(request, 'index.html', {'visualizations': visualizations})


# This route is used when a user enters their lastfm username in the modal form
def fetch_user_stats(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()

        # Save default username if the user is authenticated and checked the box
        if request.user.is_authenticated and request.POST.get('set_default_lastfm'):
            profile = request.user.siteuserprofile
            profile.default_lastfm_username = username
            profile.save()

        # Redirect to loading page
        return redirect('user_stats', username=username)

    return redirect('index')


def user_stats(request, username):
    # Fetch user's info from Lastfm API
    info = lastfmUser.get_info(username)
    user_data = info["user"]

    # Grab the avatar image and registration timestamp
    avatar = user_data["image"][-1]["#text"] if user_data.get("image") else None  # largest img
    registered_ts = user_data["registered"].get("unixtime")

    # Save/Update lasffm user entry in db
    lastfmProfile, created = LastfmUserProfile.objects.update_or_create(
        lastfm_username=username,
        defaults={
            "display_name": user_data.get("name"),
            "profile_url": user_data.get("url"),
            "avatar_url": avatar,
            "registered_date": datetime.fromtimestamp(int(registered_ts)) if registered_ts else None,
        }
    )

    # Fetch user's listening data from Last.fm
    artists = lastfmUser.get_top_artists(username, limit=5)
    albums = lastfmUser.get_top_albums(username, limit=5)
    tracks = lastfmUser.get_top_tracks(username, limit=10)
    recent = lastfmUser.get_recent_tracks(username, limit=10)

    # Create context for template rendering
    context = {
        "profile": lastfmProfile,
        "total_scrobbles": info["user"]["playcount"],
        "recent_tracks": recent["recenttracks"]["track"],
        "top_artists": artists["topartists"]["artist"],
        "top_albums": albums["topalbums"]["album"],
        "top_tracks": tracks["toptracks"]["track"],
    }

    return render(request, "user_stats.html", context)

'''
# Just a dummy route for testing viz generation
def demo_visualization(request):
    # Get a temporary hardcoded Lastfm_User_Profile object to use for required fields
    # Future: Pull Lastfm username from the request object
    lastfmProfile = LastfmUserProfile.objects.get(lastfm_username='shazamuel89')

    # Future: Extract filters/options from the request object
    # Future: Apply filters/options to Lastfm API calls

    # Fetch data from the Lastfm API based on options and filters (hard-coded for now)
    data = get_lastfm_demo_data()

    # Make the data-fed streamgraph
    fig = create_data_fed_streamgraph(data)
    # Create the empty db entry
    viz = Visualization.objects.create(
        lastfm_user=lastfmProfile,
        visualization_type='demo_streamgraph'
    )
    # Save the figure to the db
    save_plotly_figure(fig, viz)

    # Set the context
    context = {
        "plotly_json": viz.plotly_json,
        "username": "shazamuel89",
    }

    # Render the result page with the dummy visualization
    return render(request, "visualization_result.html", context)
'''

def visualization_options(request, username):
    if request.method == "POST":
        form = VisualizationOptionsForm(request.POST)
        if form.is_valid():
            # Get data from form
            viz_type = form.cleaned_data["visualization_type"]
            target = form.cleaned_data["visualization_target"]
            time_range = form.cleaned_data["time_range"]
            limit = int(form.cleaned_data["limit"])

            # Retrieve lastfm profile previously saved in db
            lastfmProfile = get_object_or_404(
                LastfmUserProfile,
                lastfm_username=username
            )

            # Create the new visualization entry in the db
            viz = Visualization.objects.create(
                lastfm_user=lastfmProfile,
                visualization_type=viz_type
            )

            # Future: Extract filters/options from the request object
            # Future: Apply filters/options to Lastfm API calls

            # Fetch data from the Lastfm API based on options and filters (hard-coded for now)
            data = get_lastfm_data(
                username=username,
                target=target,
                time_range=time_range,
                limit=limit,
            )

            # Make the data-fed streamgraph
            fig = create_data_fed_streamgraph(data)

            # Save the figure to the db
            save_plotly_figure(fig, viz)

            return redirect(
                "visualization_result",
                username=username,
                visualization_id=viz.id,
            )

    else:
        form = VisualizationOptionsForm()

    return render(request, "visualization_options.html", {
        "form": form,
        "username": username,
    })


def visualization_result(request, username, visualization_id):
    # Get the visualization from the db
    viz = get_object_or_404(Visualization, id=visualization_id)

    # Extract and pass the plotly json graph and username
    context = {
        'plotly_json': viz.plotly_json,
        'username': username,
    }

    return render(request, 'visualization_result.html', context)


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