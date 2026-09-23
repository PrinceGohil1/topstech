from django.urls import path
from . import views

urlpatterns = [
    path("music-weather/<city>/",views.music_weather),
    path("food-location/", views.food_location),
    path('country-info/<country_name>/', views.country_info),
    path('github_repos/<username>/', views.github_repos)
]