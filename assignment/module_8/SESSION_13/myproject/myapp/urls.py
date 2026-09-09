from django.urls import path
from . import views

urlpatterns = [

    # Question 1
    path("", views.index, name="index"),

    # Question 2
    path("products/", views.products, name="products"),
    path(
        "delete-product/<int:id>/",
        views.delete_product,
        name="delete_product"
    ),

    # Question 3
    path(
        "watch-later/",
        views.watch_later,
        name="watch_later"
    ),
    path(
        "delete-movie/<int:id>/",
        views.delete_movie,
        name="delete_movie"
    ),

    # Question 4
    path(
        "delete-playlist/<int:id>/",
        views.delete_playlist,
        name="delete_playlist"
    ),
]