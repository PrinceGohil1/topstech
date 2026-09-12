from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('restaurants/', views.restaurant_list, name='restaurant_list'),

    path(
        'restaurant/<int:id>/',
        views.restaurant_detail,
        name='restaurant_detail'
    ),

    path('register/', views.register, name='register'),

    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('menu/', views.menu_list, name='menu_list'),

    path(
        'order/<int:restaurant_id>/',
        views.place_order,
        name='place_order'
    ),

    path(
        'order-detail/<int:id>/',
        views.order_detail,
        name='order_detail'
    ),

    path('my-orders/', views.my_orders, name='my_orders'),
]