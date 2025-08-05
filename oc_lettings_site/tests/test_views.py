import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from oc_lettings_site.models import Letting, Address, Profile


@pytest.mark.django_db
def test_index_view(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert b"<html" in response.content.lower()


@pytest.mark.django_db
def test_lettings_index_view(client):
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200
    assert b"Lettings" in response.content or b"<html" in response.content


@pytest.mark.django_db
def test_letting_view(client):
    address = Address.objects.create(
        number=12,
        street="Main St",
        city="TestCity",
        state="TS",
        zip_code=12345,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    url = reverse('letting', args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
    assert b"Test Letting" in response.content


@pytest.mark.django_db
def test_profiles_index_view(client):
    response = client.get(reverse('profiles_index'))
    assert response.status_code == 200
    assert b"Profiles" in response.content or b"<html" in response.content


@pytest.mark.django_db
def test_profile_view(client):
    user = User.objects.create(username="jane")
    Profile.objects.create(user=user, favorite_city="Paris")
    url = reverse('profile', args=["jane"])
    response = client.get(url)
    assert response.status_code == 200
    assert b"Paris" in response.content
