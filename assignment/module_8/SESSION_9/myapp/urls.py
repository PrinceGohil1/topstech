from django.urls import path
from .views import (
    home,
    test_email,
    send_password_reset_email,
    send_order_confirmation,
    send_ipl_welcome_email,
)

urlpatterns = [

    # Home — shows all 4 forms
    path("", home, name="home"),

    # Q1 — Test email
    path("test-email/", test_email, name="test_email"),

    # Q2 — Password reset email
    path("send-reset-email/", send_password_reset_email, name="send_reset_email"),

    # Q3 + Q4 — Order confirmation HTML email
    path("order-email/", send_order_confirmation, name="order_email"),

    # Q5 — IPL Fantasy welcome email
    path("ipl-email/", send_ipl_welcome_email, name="ipl_email"),
]
