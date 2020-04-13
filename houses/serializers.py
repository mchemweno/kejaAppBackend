from rest_framework import serializers
from .models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class HouseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = House
        geo_field = 'location'
        fields = '__all__'
