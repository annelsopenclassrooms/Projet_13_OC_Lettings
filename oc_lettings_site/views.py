from django.shortcuts import render
from django.http import HttpResponse  # to test an error 500


def index(request):
    return render(request, 'index.html')


def trigger_error(request):
    1 / 0  # division by zero to trigger an error 500
    return HttpResponse("Pour tester l'erreur 500")  # never reached