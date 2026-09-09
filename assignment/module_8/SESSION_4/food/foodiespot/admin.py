from django.contrib import admin

# Register your models here.
from .models import Restaurant, coisine

admin.site.register(Restaurant)
admin.site.register(coisine)