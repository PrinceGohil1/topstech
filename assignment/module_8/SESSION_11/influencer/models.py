from django.db import models
from django.contrib.auth.models import User


class InfluencerProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    display_name = models.CharField(
        max_length=100
    )

    bio = models.TextField(
        blank=True
    )

    phone_number = models.CharField(
        max_length=10
    )

    profile_pic = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.display_name