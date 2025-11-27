from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from .forms import RegisterForm


def index(request):
    return render(request, 'index.html')


def fetch_user_stats(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        # Redirect to loading page while fetching stats from Last.fm
        return redirect('loading_user_stats', username=username)

    # Keep index redirect to cover any potential edge cases
    return redirect('index')

def loading_user_stats(request, username):
    return render(request, 'loading_user_stats.html', {'username': username})


def user_stats(request, username):
    return render(request, 'user_stats.html', {'username': username})


def visualization_options(request, username):
    return render(request, 'visualization_options.html', {'username': username})


def loading_visualization(request, visualization_id):
    return render(request, 'loading_visualization.html', {'id': visualization_id})


def visualization_result(request, visualization_id):
    return render(request, 'visualization_result.html', {'id': visualization_id})


@login_required
def account(request):
    return render(request, 'account.html')


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
