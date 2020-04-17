from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from drf_extra_fields.geo_fields import PointField


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'


class HouseSerializer(GeoFeatureModelSerializer):
    location = PointField()

    class Meta:
        model = House
        geo_field = 'location'
        fields = ('name', 'category', 'rooms', 'price', 'amenities', 'master_image', 'owner')


class HouseImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImages
        fields = '__all__'
