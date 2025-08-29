from django.contrib import admin
from lettings.models import Letting, Address

"""Register Letting and Address models in the Django admin."""

admin.site.register(Letting)
admin.site.register(Address)
