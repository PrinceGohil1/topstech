from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MenuItem


def menu_list(request):

    menu_items = MenuItem.objects.filter(
        price__gt=150
    ).order_by("price")

    paginator = Paginator(menu_items, 3)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "menu_list.html",
        {
            "page_obj": page_obj
        }
    )