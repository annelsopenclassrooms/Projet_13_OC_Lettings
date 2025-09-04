import sentry_sdk
from django.shortcuts import render, get_object_or_404
from .models import Profile

"""Views for the profiles app with Sentry integration."""


def index(request):  # profiles_index before
    """
    Display all profiles.

    Fetches all profiles from the database and renders them in the index template.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Display a specific user's profile.

    Fetches a profile by the associated user's username and renders it.
    If the profile does not exist, a 404 error page is returned.
    Any unexpected errors are reported to Sentry.
    """
    try:
        profile_obj = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile_obj}
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        # Report unexpected errors to Sentry
        sentry_sdk.capture_exception(e)
        raise
