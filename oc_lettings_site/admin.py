from django.contrib import admin
from lettings.models import Letting, Address
from profiles.models import Profile

"""Register models to the Django admin site."""

admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
