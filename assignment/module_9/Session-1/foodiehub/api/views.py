from django.http import JsonResponse

def hello_spotify(request):
    return JsonResponse({"message": "Hello, Spotify Fans!"})