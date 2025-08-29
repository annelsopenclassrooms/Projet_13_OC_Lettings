from django.urls import path
from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]

"""
URL patterns for the lettings app.

- index: lists all lettings.
- letting: shows details for a single letting identified by letting_id.
"""
