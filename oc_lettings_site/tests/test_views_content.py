import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from oc_lettings_site.models import Letting, Address, Profile


@pytest.mark.django_db
def test_index_contains_titles_and_links(client):
    response = client.get(reverse('index'))
    content = response.content.decode()
    assert "<h1" in content
    assert "Welcome to Holiday Homes" in content
    assert reverse('profiles_index') in content
    assert reverse('lettings_index') in content


@pytest.mark.django_db
def test_lettings_index_displays_lettings(client):
    address = Address.objects.create(
        number=1, street="Main", city="Paris", state="IDF", zip_code=75000, country_iso_code="FR"
    )
    Letting.objects.create(title="Ocean Villa", address=address)
    response = client.get(reverse('lettings_index'))
    content = response.content.decode()
    assert "Lettings" in content
    assert "Ocean Villa" in content
    assert reverse('letting', args=[1]) in content


@pytest.mark.django_db
def test_letting_detail_contains_address(client):
    address = Address.objects.create(
        number=10, street="Rue Victor Hugo", city="Lyon", state="ARA", zip_code=69000, country_iso_code="FR"
    )
    letting = Letting.objects.create(title="Villa Lumière", address=address)
    response = client.get(reverse('letting', args=[letting.id]))
    content = response.content.decode()
    assert "Villa Lumière" in content
    assert "Rue Victor Hugo" in content
    assert "Lyon" in content
    assert "FR" in content


@pytest.mark.django_db
def test_profiles_index_displays_profiles(client):
    user = User.objects.create(username="emma", first_name="Emma", last_name="Stone", email="emma@example.com")
    Profile.objects.create(user=user, favorite_city="Nice")
    response = client.get(reverse('profiles_index'))
    content = response.content.decode()
    assert "Profiles" in content
    assert "emma" in content
    assert reverse('profile', args=["emma"]) in content


@pytest.mark.django_db
def test_profile_detail_displays_info(client):
    user = User.objects.create(
        username="john",
        first_name="John",
        last_name="Doe",
        email="john@example.com"
    )
    Profile.objects.create(user=user, favorite_city="Bordeaux")
    response = client.get(reverse('profile', args=["john"]))
    content = response.content.decode()
    assert "john" in content
    assert "John" in content
    assert "Doe" in content
    assert "john@example.com" in content
    assert "Bordeaux" in content
