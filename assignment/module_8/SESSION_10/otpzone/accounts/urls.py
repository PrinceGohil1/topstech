from django.urls import path
from . import views


urlpatterns = [

    path(
        'forgot-password/',
        views.forgot_password_view,
        name='forgot_password'
    ),

    path(
        'verify-otp/',
        views.verify_otp,
        name='verify_otp'
    ),
]