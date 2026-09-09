from django.shortcuts import render
from .models import Restaurant


def restaurant_list(request):
    restaurants = Restaurant.objects.filter(rating__gt=4.0)

    print(restaurants)
    print(restaurants.count())

    return render(request, "restaurant.html", {
        "restaurants": restaurants
    })