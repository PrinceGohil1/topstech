from django.urls import path
from . import views

urlpatterns = [
    path('add_restaurant/',views.add_restaurant,name='add_restaurant'),
    path('success/',views.restaurant_success,name='restaurant_success'),
]