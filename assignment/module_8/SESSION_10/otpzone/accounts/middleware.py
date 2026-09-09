from django.shortcuts import redirect


class BlockExpiredOTPAccessMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        if request.path == '/verify-otp/':

            otp = request.session.get('otp')

            if not otp:

                return redirect('forgot_password')

        response = self.get_response(request)

        return response