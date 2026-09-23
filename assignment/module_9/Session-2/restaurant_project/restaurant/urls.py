from django.urls import path
from .views import (ResturantListCreateAPIView,ResturantDetailAPIView)

urlpatterns = [
    path('restaurants/',ResturantListCreateAPIView.as_view()),
    path('restaurants/<int:pk>/',ResturantDetailAPIView.as_view()),
]