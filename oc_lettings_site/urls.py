from django.contrib import admin
from django.urls import path, include
from . import views

"""Root URL configuration for the project."""

urlpatterns = [
    path('', views.index, name='index'),  # main homepage
    path('lettings/', include(('lettings.urls', 'lettings'), namespace='lettings')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
    path("trigger-error/", views.trigger_error, name="trigger_error"),
]
