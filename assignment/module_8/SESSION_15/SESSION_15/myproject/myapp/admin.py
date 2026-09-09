from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, MovieReview, Playlist


# Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")


# Movie Review
@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = ("movie_name", "review")


# Playlist - Only Admin Group
@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):

    def has_view_permission(self, request, obj=None):
        return request.user.groups.filter(name="Admin").exists()

    def has_add_permission(self, request):
        return request.user.groups.filter(name="Admin").exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name="Admin").exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name="Admin").exists()