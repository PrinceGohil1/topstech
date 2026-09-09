from django.db import models

# Create your models here.
class coisine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    rating = models.FloatField()
    coisine = models.ForeignKey(coisine,on_delete=models.CASCADE)

