from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Visualization, LastfmUserProfile, SiteUserProfile

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
    # Render page
    # Fetch user's profile data from db and Last.fm
    # Upon finishing fetching, redirect to user_stats page
    return render(request, 'loading_user_stats.html', {'username': username})


def user_stats(request, username):
    return render(request, 'user_stats.html', {'username': username})


def visualization_options(request, username):
    # On POST, send visualization options data to backend which creates an empty viz entry in the db and returns the id
    # Then render loading page with the id
    return render(request, 'visualization_options.html', {'username': username})


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


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # automatically log them in
            return redirect('account')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
