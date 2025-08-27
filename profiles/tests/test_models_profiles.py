import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_str():
    user = User.objects.create(username="watson")
    profile = Profile.objects.create(user=user, favorite_city="Paris")
    assert str(profile) == "watson"
