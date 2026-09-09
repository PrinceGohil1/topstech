from django.db import models


# Task 2 - Product
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Task 3 - Movie Review
class MovieReview(models.Model):
    movie_name = models.CharField(max_length=100)
    review = models.TextField()

    def __str__(self):
        return self.movie_name


# Task 5 - Playlist
class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name