from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Restaurant, MenuItem, Order, OrderItem


# Home
def home(request):
    restaurants = Restaurant.objects.all()

    return render(request, 'home.html', {
        'restaurants': restaurants
    })


# Restaurant List
def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    return render(request, 'restaurant_list.html', {
        'restaurants': restaurants
    })


# Restaurant Detail
def restaurant_detail(request, id):
    restaurant = get_object_or_404(
        Restaurant,
        id=id
    )

    menu_items = MenuItem.objects.filter(
        restaurant=restaurant,
        available=True
    )

    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'menu_items': menu_items
    })


# Register
def register(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        login(request, user)

        return redirect('restaurant_list')

    return render(request, 'register.html')


# Login
def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            return redirect('restaurant_list')

        return render(request, 'login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'login.html')


# Logout
@login_required
def user_logout(request):
    logout(request)

    return redirect('home')


# Menu List
def menu_list(request):
    menu_items = MenuItem.objects.filter(
        available=True
    )

    return render(request, 'menu_list.html', {
        'menu_items': menu_items
    })


# Place Order
@login_required
def place_order(request, restaurant_id):

    restaurant = get_object_or_404(
        Restaurant,
        id=restaurant_id
    )

    menu_items = MenuItem.objects.filter(
        restaurant=restaurant,
        available=True
    )

    if request.method == 'POST':

        order = Order.objects.create(
            customer=request.user,
            total_amount=0
        )

        total = 0

        for item in menu_items:

            quantity = int(
                request.POST.get(
                    f'quantity_{item.id}',
                    0
                )
            )

            if quantity > 0:

                OrderItem.objects.create(
                    order=order,
                    menu_item=item,
                    quantity=quantity,
                    price=item.price
                )

                total += item.price * quantity

        order.total_amount = total
        order.save()

        return redirect(
            'order_detail',
            id=order.id
        )

    return render(request, 'place_order.html', {
        'restaurant': restaurant,
        'menu_items': menu_items
    })


# Order Detail
@login_required
def order_detail(request, id):

    order = get_object_or_404(
        Order,
        id=id,
        customer=request.user
    )

    items = OrderItem.objects.filter(
        order=order
    )

    return render(request, 'order_detail.html', {
        'order': order,
        'items': items
    })


# My Orders
@login_required
def my_orders(request):

    orders = Order.objects.filter(
        customer=request.user
    ).order_by('-order_date')

    return render(request, 'my_orders.html', {
        'orders': orders
    })