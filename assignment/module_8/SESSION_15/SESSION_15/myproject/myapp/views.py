from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


# 1. My Orders
@login_required
def my_orders(request):
    return render(request, "my_orders.html")


# 2. Seller - Post Product
@login_required
@permission_required("myapp.add_product", raise_exception=True)
def post_product(request):
    return render(request, "post_product.html")


# 3. Movie Reviews
@login_required
def movie_reviews(request):

    if request.user.has_perm("myapp.add_moviereview"):
        return render(request, "movie_reviews.html")

    elif request.user.has_perm("myapp.view_moviereview"):
        return render(request, "movie_reviews.html")

    else:
        return render(request, "permission_denied.html")


# 4. Role Based Dashboard
@login_required
def dashboard(request):

    if request.user.groups.filter(name="Seller").exists():
        return render(request, "seller_dashboard.html")

    elif request.user.groups.filter(name="Buyer").exists():
        return render(request, "buyer_dashboard.html")

    else:
        return render(request, "permission_denied.html")


# 5. Playlist - Only Admin Group
@login_required
def playlist(request):

    if request.user.groups.filter(name="Admin").exists():
        return render(request, "playlist.html")

    else:
        return render(request, "permission_denied.html")