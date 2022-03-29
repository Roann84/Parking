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
import re

# @api_view(['GET', 'POST'])
# def cars_list(request):
#     if request.method == 'GET':
#         queryset = models.Cars.objects.all()
#         serializer = CarsSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CarsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def cars_list(request):
    if request.method == 'GET':
        queryset = models.Cars.objects.all()
        serializer = CarsSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = request.POST.get('plate', request.data)
        if len(str(serializer)) == 21:
            p = re.compile(r'([A-Z][A-Z][A-Z])-([0-9][0-9][0-9][0-9])')
            if bool(re.search(p, str(serializer))):
                serializer1 = CarsSerializer(data=request.data)
                if serializer1.is_valid():
                    serializer1.save()
                    return Response(serializer1.data, status=status.HTTP_201_CREATED)
                return Response(status=status.status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

# if plate.is_valid():

# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def change_and_delete(request, pk):
    try:
        car_id = models.Cars.objects.get(pk=pk)
    except models.Cars.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarsSerializer(car_id)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CarsSerializer(car_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        car_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
