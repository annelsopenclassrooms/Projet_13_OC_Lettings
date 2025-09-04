import sentry_sdk
from django.shortcuts import render, get_object_or_404
from .models import Letting

"""Views for the lettings app with Sentry integration."""


def index(request):  # lettings_index before
    """
    Display all lettings.

    Fetches all lettings from the database and renders them in the index template.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Display a single letting.

    Fetches a letting by its ID and renders its title and address in the detail template.
    If the letting does not exist, a 404 error page is returned.
    Any unexpected errors are reported to Sentry.
    """
    try:
        letting_obj = get_object_or_404(Letting, id=letting_id)
        context = {
            'title': letting_obj.title,
            'address': letting_obj.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Exception as e:
        # Report unexpected errors to Sentry
        sentry_sdk.capture_exception(e)
        raise
