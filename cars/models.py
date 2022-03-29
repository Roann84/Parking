from math import fabs
from pickle import TRUE
from django.db import models

# Create your models here.


class Cars(models.Model):
    id_car = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=8, unique=True)
    time = models.CharField(max_length=255, blank=True)
    paid = models.BooleanField(default=False)
    left = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)
