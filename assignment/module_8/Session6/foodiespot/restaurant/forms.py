from django import forms
from django.core.validators import MinLengthValidator


class AddRestaurantForm(forms.Form):
    restaurant_name = forms.CharField(
        label="Restaurant Name",
        max_length=100,
        validators=[MinLengthValidator(3)],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter restaurant name"
            }
        )
    )

    cuisine_type = forms.CharField(
        label="Cuisine Type",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter cuisine type"
            }
        )
    )

    contact_email = forms.EmailField(
        label="Contact Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter contact email"
            }
        )
    )