from django.db import models
from django.contrib.auth.models import User


# Task 1: Playlist
class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Task 2: Order
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product


# Task 3: Cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.item


# Task 4: Premium User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# Task 4: Ticket
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.subject