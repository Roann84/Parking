from django.urls import path
from cars.views import Cars_List, Cars_Out, Cars_Pay, Cars_Plate


urlpatterns = [
    path('', Cars_List.as_view()),
    path('<int:pk>/out/', Cars_Out.as_view()),
    path('<int:pk>/pay/', Cars_Pay.as_view()),
    path('<str:plate>/', Cars_Plate.as_view()),
]
