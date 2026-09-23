from django.urls import path
from .views import PlaylistView, OrderView, CartView, TicketView


urlpatterns = [
    path('playlists/', PlaylistView.as_view(), name='playlists'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('cart/', CartView.as_view(), name='cart'),
    path('tickets/', TicketView.as_view(), name='tickets'),
]