from django.urls import path
from cars.views import cars_list, change_and_delete


urlpatterns = [
    path('', cars_list),
    path('<int:pk>/', change_and_delete),
]
