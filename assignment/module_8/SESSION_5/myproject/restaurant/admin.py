from django.contrib import admin
from .models import Resturant

# Register your models here.
@admin.register(Resturant)

class ResturantAdmin(admin.ModelAdmin):
    list_display = ['name', 'cuisine', 'rating']
    search_fields = ['name', 'cuisine']
    list_filter = ['cuisine']