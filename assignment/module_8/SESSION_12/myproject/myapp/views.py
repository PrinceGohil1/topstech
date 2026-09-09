from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


# Add + Product List
def product_list(request):

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()

    products = Product.objects.all()

    return render(request, 'product_list.html', {
        'form': form,
        'products': products
    })


# Edit Product
def edit_product(request, id):

    product = Product.objects.get(id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {
        'form': form,
        'product': product
    })


# Delete Product
def delete_product(request, id):

    product = Product.objects.get(id=id)

    if request.method == "POST":
        product.delete()
        return redirect('product_list')

    return render(request, 'delete_product.html', {
        'product': product
    })