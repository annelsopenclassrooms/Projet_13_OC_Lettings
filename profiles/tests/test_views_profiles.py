import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

@pytest.mark.django_db
def test_profiles_index_view(client):
    user = User.objects.create(username="emma", first_name="Emma", last_name="Stone")
    Profile.objects.create(user=user, favorite_city="Nice")
    response = client.get(reverse("profiles:index"))
    assert response.status_code == 200
    assert b"Profiles" in response.content

@pytest.mark.django_db
def test_profile_detail_view(client):
    user = User.objects.create(username="john")
    Profile.objects.create(user=user, favorite_city="Bordeaux")
    url = reverse("profiles:profile", args=["john"])
    response = client.get(url)
    assert response.status_code == 200
    assert b"Bordeaux" in response.content
    assert b"john" in response.content
