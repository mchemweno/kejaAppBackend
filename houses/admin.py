from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import House


# Register your models here.
admin.site.register(House, LeafletGeoAdmin);
