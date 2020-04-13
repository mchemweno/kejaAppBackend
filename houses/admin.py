from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import *


# Register your models here.
admin.site.register(House, LeafletGeoAdmin)
admin.site.register(Dstv)
admin.site.register(Wifi)
admin.site.register(Rooms)
admin.site.register(Category)
