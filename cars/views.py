from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from cars.serializers import CarsSerializer
from cars import models
import re


class Cars_List(APIView):
    def get(self, request):
        queryset = models.Cars.objects.all()
        serializer = CarsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        plate = request.POST.get('plate', request.data)
        if len(str(plate)) == 21:
            p = re.compile(r'([A-Z][A-Z][A-Z])-([0-9][0-9][0-9][0-9])')
            if bool(re.search(p, str(plate))):
                serializer = CarsSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(status=status.HTTP_411_LENGTH_REQUIRED)


class Cars_Out(APIView):

    def get_object(self, pk):
        try:
            return models.Cars.objects.get(pk=pk)
        except models.Cars.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        car_id = self.get_object(pk)
        serializer = CarsSerializer(car_id)
        return Response(serializer.data)

    def put(self, request, pk):
        car_id = self.get_object(pk)
        serializer = CarsSerializer(car_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        car_id = self.get_object(pk)
        car_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Cars_Pay(APIView):
    def get_object(self, pk):
        try:
            return models.Cars.objects.get(pk=pk)
        except models.Cars.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        car_id = self.get_object(pk)
        serializer = CarsSerializer(car_id)
        return Response(serializer.data)


class Cars_Plate(APIView):
    def get_object(self, plate):
        try:
            return models.Cars.objects.get(plate=plate)
        except models.Cars.DoesNotExist:
            raise NotFound()

    def get(self, request, plate):
        car_plate = self.get_object(plate)
        serializer = CarsSerializer(car_plate)
        return Response(serializer.data)
