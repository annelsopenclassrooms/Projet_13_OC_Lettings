import pytest
from lettings.models import Address, Letting

@pytest.mark.django_db
def test_address_str():
    address = Address.objects.create(
        number=42,
        street="Elm Street",
        city="Springfield",
        state="SP",
        zip_code=54321,
        country_iso_code="USA"
    )
    assert str(address) == "42 Elm Street"

@pytest.mark.django_db
def test_letting_str():
    address = Address.objects.create(
        number=1,
        street="Baker Street",
        city="London",
        state="LD",
        zip_code=12345,
        country_iso_code="GBR"
    )
    letting = Letting.objects.create(title="Sherlock's Home", address=address)
    assert str(letting) == "Sherlock's Home"
