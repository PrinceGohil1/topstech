from django.shortcuts import render
from .models import Restaurant, MenuItem, Order


def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    return render(
        request,
        "restaurant_list.html",
        {"restaurants": restaurants}
    )


def menu_list(request):
    menu_items = MenuItem.objects.all()

    return render(
        request,
        "menu_list.html",
        {"menu_items": menu_items}
    )


def order_list(request):
    orders = Order.objects.all()

    return render(
        request,
        "order_list.html",
        {"orders": orders}
    )