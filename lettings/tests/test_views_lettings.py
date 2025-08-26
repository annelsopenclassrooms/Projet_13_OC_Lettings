import pytest
from django.urls import reverse
from lettings.models import Address, Letting

@pytest.mark.django_db
def test_lettings_index_view(client):
    response = client.get(reverse("lettings:index"))
    assert response.status_code == 200
    assert b"Lettings" in response.content or b"<html" in response.content

@pytest.mark.django_db
def test_letting_detail_view(client):
    address = Address.objects.create(
        number=12,
        street="Main St",
        city="TestCity",
        state="TS",
        zip_code=12345,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    url = reverse("lettings:letting", args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
    assert b"Test Letting" in response.content
    assert bytes(address.street, "utf-8") in response.content
