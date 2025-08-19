from django.urls import path
from . import views

app_name = 'profiles'  # namespace for the app
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
