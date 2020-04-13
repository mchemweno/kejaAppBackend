from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'

class HouseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = House
        geo_field = 'location'
        fields = '__all__'
