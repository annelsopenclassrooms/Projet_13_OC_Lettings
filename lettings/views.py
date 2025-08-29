from django.shortcuts import render
from .models import Letting


# Create your views here.


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
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
