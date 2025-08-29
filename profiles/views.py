from django.shortcuts import render
from .models import Profile


# Create your views here.

def index(request):  # profils_index before
    """Display a list of all profiles."""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Display the profile for a specific user by username."""
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
