from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Movie



# QUESTION 1
# Spotify Playlist


def index(request):
    return render(request, "index.html")



# QUESTION 2
# Flipkart Wishlist


def products(request):

    products = Product.objects.all()

    return render(request, "products.html", {
        "products": products
    })


def delete_product(request, id):

    if request.method == "DELETE":

        try:
            product = Product.objects.get(id=id)
            product.delete()

            return JsonResponse({
                "success": True,
                "message": "Product removed from wishlist!"
            })

        except Product.DoesNotExist:

            return JsonResponse({
                "success": False,
                "message": "Product not found!"
            })

    return JsonResponse({
        "success": False,
        "message": "Invalid request!"
    })



# QUESTION 3
# BookMyShow Watch Later


def watch_later(request):

    movies = Movie.objects.all()

    return render(request, "watch_later.html", {
        "movies": movies
    })


def delete_movie(request, id):

    if request.method == "DELETE":

        movie = Movie.objects.get(id=id)

        movie.delete()

        return JsonResponse({
            "success": True,
            "message": "Movie removed from Watch Later!"
        })

    return JsonResponse({
        "success": False,
        "message": "Invalid request!"
    })



# QUESTION 4
# Playlist Delete


def delete_playlist(request, id):

    if request.method == "DELETE":

        return JsonResponse({
            "success": True,
            "message": "Playlist deleted successfully!"
        })

    return JsonResponse({
        "success": False
    })