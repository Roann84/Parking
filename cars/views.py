# from rest_framework import viewsets
# from cars.serializer import CarsSerializer
# from cars import models


# class CarsViewSet(viewsets.ModelViewSet):
#     serializer_class = CarsSerializer
#     queryset = models.Cars.objects.all()

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cars.serializers import CarsSerializer
from cars import models


@api_view(['GET', 'POST'])
def cars_list(request):
    if request.method == 'GET':
        queryset = models.Cars.objects.all()
        serializer = CarsSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def change_delete()
