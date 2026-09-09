from django.urls import path
from . import views


urlpatterns = [
    path("add-restaurant/",views.add_restaurant,name="add_restaurant"),
]