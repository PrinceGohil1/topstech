from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import (
    Restaurant,
    MenuItem,
    Order,
    OrderItem
)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'restaurant',
        'price',
        'available'
    )
    search_fields = ('name',)
    list_filter = ('available', 'restaurant')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'order_date',
        'total_amount'
    )
    search_fields = ('customer__username',)
    list_filter = ('order_date',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'menu_item',
        'quantity',
        'price'
    )
    search_fields = ('menu_item__name',)
    list_filter = ('menu_item',)