from django.shortcuts import render, redirect
from .forms import RestaurantForm

def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_success')
    else:
        form = RestaurantForm()
    return render(request,'restaurants/add_restaurant.html',{'form': form})

def restaurant_success(request):
    return render(request,'restaurants/restaurant_success.html')