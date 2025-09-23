import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    response = client.get(reverse("index"))
    assert response.status_code == 200
    content = response.content.decode()
    assert "<h1" in content
    assert "Welcome to OC" in content
    assert reverse("profiles:index") in content
    assert reverse("lettings:index") in content
