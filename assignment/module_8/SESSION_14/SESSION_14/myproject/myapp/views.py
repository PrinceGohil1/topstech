from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
    restaurants = Restaurant.objects.filter(
        cuisine="Chinese",
        rating__gt=4
    )

    return render(request, "restaurant.html", {
        "restaurants": restaurants
    })