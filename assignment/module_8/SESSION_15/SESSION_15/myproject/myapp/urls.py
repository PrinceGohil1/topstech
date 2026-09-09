from django.urls import path
from . import views

urlpatterns = [

    # 1. My Orders
    path("my-orders/", views.my_orders, name="my_orders"),

    # 2. Post Product
    path("post-product/", views.post_product, name="post_product"),

    # 3. Movie Reviews
    path("movie-reviews/", views.movie_reviews, name="movie_reviews"),

    # 4. Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),

    # 5. Playlist
    path("playlist/", views.playlist, name="playlist"),
]