from django.db import models

# Create your models here.


class Cars(models.Model):
    id_car = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=8)
    time = models.CharField(max_length=255)
    paid = models.BooleanField()
    left = models.BooleanField()
    create_date = models.DateField(auto_now_add=True)
