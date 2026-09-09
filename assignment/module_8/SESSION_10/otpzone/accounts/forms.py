from django import forms

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email Address')

class OTPVerificationForm(forms.Form):
    otp = forms.CharField(max_length=6,min_length=6,label='Enter OTP')