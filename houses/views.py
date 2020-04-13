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
    print(serializer)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
