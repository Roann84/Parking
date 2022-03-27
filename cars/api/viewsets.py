from rest_framework import viewsets
from cars.api import serializers
from cars import models


class CarsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CarsSerializer
    queryset = models.Cars.objects.all()
