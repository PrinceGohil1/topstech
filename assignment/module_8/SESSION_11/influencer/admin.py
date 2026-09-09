from django.contrib import admin
from .models import InfluencerProfile
# Register your models here.



@admin.register(InfluencerProfile)
class InfluencerProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'display_name',
        'profile_pic',
    )