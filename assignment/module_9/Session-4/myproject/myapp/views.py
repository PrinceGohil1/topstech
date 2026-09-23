from rest_framework.views import APIView
from rest_framework.authentication import (
    BasicAuthentication,
    TokenAuthentication,
    SessionAuthentication
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Playlist, Order, Cart, Ticket
from .serializers import (
    PlaylistSerializer,
    OrderSerializer,
    CartSerializer,
    TicketSerializer
)
from .permissions import IsPremiumUser


# Task 1: Basic Authentication
class PlaylistView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        playlist = Playlist.objects.all()
        serializer = PlaylistSerializer(playlist, many=True)
        return Response(serializer.data)


# Task 2: Token Authentication
class OrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


# Task 3: Session Authentication
class CartView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
             serializer.save(user=request.user)
             return Response(serializer.data)

        return Response(serializer.errors)


# Task 4: Premium User Permission
class TicketView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsPremiumUser]

    def post(self, request):
        serializer = TicketSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)

        return Response(serializer.errors)