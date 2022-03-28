from django.urls import path
from cars.views import cars_list


urlpatterns = [
    path('', cars_list),
]
