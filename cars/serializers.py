from rest_framework import serializers
from cars import models


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cars
        fields = ['id_car', 'plate', 'time', 'paid', 'left', 'create_date']
        #fields = '__all__'
