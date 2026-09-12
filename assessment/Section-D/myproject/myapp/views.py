from django.http import JsonResponse
from .models import Restaurant, MenuItem


def menu_api(request, restaurant_id):

    # Authentication check
    if not request.user.is_authenticated:
        return JsonResponse(
            {"message": "Authentication required"},
            status=403
        )

    # Restaurant check
    try:
        restaurant = Restaurant.objects.get(id=restaurant_id)
    except Restaurant.DoesNotExist:
        return JsonResponse(
            {"error": "Restaurant not found"},
            status=404
        )

    # Available menu items
    menu_items = MenuItem.objects.filter(
        restaurant=restaurant,
        available=True
    )

    # max_price filter
    max_price = request.GET.get("max_price")

    if max_price:
        menu_items = menu_items.filter(price__lte=max_price)

    # Convert to JSON data
    data = list(
        menu_items.values(
            "name",
            "price",
            "category"
        )
    )

    return JsonResponse(data, safe=False)