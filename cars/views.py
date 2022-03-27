from rest_framework import viewsets
from cars.serializer import CarsSerializer
from cars import models


class CarsViewSet(viewsets.ModelViewSet):
    serializer_class = CarsSerializer
    queryset = models.Cars.objects.all()
