import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import (
    ForgotPasswordForm,
    OTPVerificationForm
)


def forgot_password_view(request):

    if request.method == 'POST':

        form = ForgotPasswordForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']

            otp = str(random.randint(100000, 999999))

            request.session['otp'] = otp
            request.session['otp_email'] = email

            request.session.set_expiry(300)

            send_mail(
                'Password Reset OTP',
                f'Your password reset OTP is: {otp}\n\n'
                'This OTP is valid for 5 minutes.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False
            )

            return redirect('verify_otp')

    else:

        form = ForgotPasswordForm()

    return render(
        request,
        'forgot_password.html',
        {'form': form}
    )


def verify_otp(request):

    if request.method == 'POST':

        form = OTPVerificationForm(request.POST)

        if form.is_valid():

            entered_otp = form.cleaned_data['otp']

            stored_otp = request.session.get('otp')

            if stored_otp == entered_otp:

                request.session.pop('otp', None)

                return render(
                    request,
                    'otp_success.html'
                )

            else:

                return render(
                    request,
                    'verify_otp.html',
                    {
                        'form': form,
                        'message': 'Invalid OTP!'
                    }
                )

    else:

        form = OTPVerificationForm()

    return render(
        request,
        'verify_otp.html',
        {'form': form}
    )