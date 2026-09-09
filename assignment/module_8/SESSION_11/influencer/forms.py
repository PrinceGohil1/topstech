from django import forms
from .models import InfluencerProfile


class InfluencerProfileForm(forms.ModelForm):

    class Meta:
        model = InfluencerProfile

        fields = [
            'display_name',
            'bio',
            'phone_number',
            'profile_pic'
        ]