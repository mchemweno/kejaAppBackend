from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


# Create your views here.

@api_view(['GET'])
def get_houses(request):
    try:
        house = House.objects.all()
        serializer = HouseSerializer(house, many=True).data
        return Response(serializer)
    except:
        return Response([], status=404)


@api_view(['POST'])
def create_house(request):
    data = request.data
    serializer = HouseSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_houses_around_specific_point(request):
    try:
        latitude = float(request.GET.get('latitude', ''))
        longitude = float(request.GET.get('longitude', ''))
    except:
        return Response({'Error': 'Please pass the latitude and longitude as url parameters'},
                        status=status.HTTP_404_NOT_FOUND)

    user_location = Point(longitude, latitude, srid=4326)
    try:
        house = House.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:50]
        serializer = HouseSerializer(house, many=True).data
        return Response(serializer)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
