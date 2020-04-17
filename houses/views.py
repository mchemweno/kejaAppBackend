from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *

# Create your views here.
""" Views for houses:-
 1. Getting all houses. 
 2. Getting houses around a certain point
 3. Creating a house
 n/b a function for populating house_images and binding them to the res data
 """


@api_view(['GET'])
def get_houses(request):
    try:
        house = House.objects.all()
        house_serializer = HouseSerializer(house, many=True).data
        updates_houses = get_house_images(house_serializer)
        return Response(updates_houses)
    except House.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_houses_around_specific_point(request):
    try:
        latitude = float(request.GET.get('latitude', ''))
        longitude = float(request.GET.get('longitude', ''))
    except ValueError:
        return Response({'Error': 'Please pass the latitude and longitude as url parameters'},
                        status=status.HTTP_404_NOT_FOUND)

    user_location = Point(longitude, latitude, srid=4326)
    try:
        house = House.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:50]
        house_serializer = HouseSerializer(house, many=True).data
        updates_houses = get_house_images(house_serializer)
        return Response(updates_houses)
    except House.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST', 'PATCH', 'DELETE'])
def create_house(request):
    if request.method == 'POST':
        data = request.data
        serializer = HouseSerializer(data=data)
        try:
            if serializer.is_valid('raise_exception'):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as error:
            print(error)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        data = request.data
        house_id = data['id']
        try:
            house = House.objects.get(pk=house_id)
            house.location = data['location']
            house.save()
        except House.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data = request.data
        house_id = data['id']
        house = House.objects.get(pk=house_id)
        house.delete()


def get_house_images(houses_obj):
    for house in houses_obj['features']:
        house_images = HouseImages.objects.filter(house=house['id']).only('id', 'image')
        house_images_serializer = HouseImagesSerializer(house_images, many=True)
        image_link_array = []
        for image in house_images_serializer.data:
            image_link_array.append(image['image'])
        house['properties'].update(house_images=image_link_array)
    return houses_obj


"""create house images"""


@api_view(['POST'])
def create_house_image(request):
    data = request.data
    house_image_serializer = HouseImagesSerializer(data=data)
    try:
        if house_image_serializer.is_valid('raise_exception'):
            house_image_serializer.save()
            return Response(status=status.HTTP_201_CREATED)

    except serializers.ValidationError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
