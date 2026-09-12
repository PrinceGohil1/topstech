from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/menu/<int:restaurant_id>/",
        views.menu_api,
        name="menu_api"
    ),
]