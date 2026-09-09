from django.db import models

# Create your models here.

class Resturant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name
