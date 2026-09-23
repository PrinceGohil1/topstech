from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):

    queryset = Restaurant.objects.all()

    serializer_class = RestaurantSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]

    filterset_fields = ['cuisine']

    ordering_fields = ['name', 'cuisine']

    ordering = ['name']