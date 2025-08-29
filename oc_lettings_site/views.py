from django.shortcuts import render
from django.http import HttpResponse  # to test a 500 error

"""Views for the main project."""


def index(request):
    """Render the main homepage."""
    return render(request, 'index.html')


def trigger_error(request):
    """Trigger a 500 error for testing purposes."""
    1 / 0  # division by zero to trigger an error 500
    return HttpResponse("Pour tester l'erreur 500")  # never reached
