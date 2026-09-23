from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from myproject.settings import OPERN_WEATHER_API
from django.http import JsonResponse

# Create your views here.


@api_view(["GET"])
def music_weather(request,city):
    api_key = OPERN_WEATHER_API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return Response({
            "error":"city not found"
        }, status=404)

    data = response.json()
    temprature = data['main']['temp']
    description = data['weather'][0]['description']

    return Response({
        'temperature':temprature,
        'description':description
    })

@api_view(['GET'])
def food_location(request):

    restaurant = request.GET.get("restaurant")

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": restaurant,
        "format": "jsonv2",
        "limit": 1
    }

    headers = {
        "User-Agent": "Django-Food-Location-App"
    }

    response = requests.get(url, params=params, headers=headers)

    data = response.json()

    if not data:
        return Response({
            "error": "restaurant not found"
        }, status=404)

    return Response({
        "latitude": data[0]["lat"],
        "longitude": data[0]["lon"]
    })

def country_info(request,country_name):
    response = requests.get(
    f"https://api.restcountries.com/countries/v5/names.common/{country_name}",
    headers={
        "Authorization": "Bearer rc_live_demo"
    }
)

    data = response.json()
    country = data["data"]["objects"][0]

    population = country["population"]
    capital = country["capitals"][0]["name"]
    return JsonResponse({
        "population":population,
        "capital":capital
    })

def github_repos(request,username):
    response = requests.get(
        f"https://api.github.com/users/{username}/repos"
    )
    data = response.json()
    repo_names = [repo["name"] for repo in data]
    return JsonResponse({
        "repositories": repo_names
    })