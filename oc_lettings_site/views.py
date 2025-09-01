import logging
from django.shortcuts import render
from django.http import HttpResponse  # to test a 500 error

"""Views for the main project."""

logger = logging.getLogger(__name__)


def index(request):
    """Render the main homepage."""
    logger.info("Homepage accessed")
    return render(request, 'index.html')


def trigger_error(request):
    """Trigger a 500 error for testing purposes."""
    logger.error("Intentional error triggered in trigger_error view")
    1 / 0  # division by zero to trigger an error 500
    return HttpResponse("This line is never reached")
