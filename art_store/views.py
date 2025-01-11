from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import ReviewForm , UserCreationForm
from .models import Product, Review, Order
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout, user_logged_in


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})

def index(request):
    products = Product.objects.all()

    user = request.user

    return render(request, 'index.html', {'products': products , 'user': user})


def details(request , product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'Product_Details.html', {'product': product})

@login_required
def add_review(request, product_id):
    product = Product.objects.get(id=product_id)
    #if not request.user.is_authenticated:
        #return HttpResponseForbidden("You must be logged in to add a review.")
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.User = request.user
            review.save()
        else:
            print(form.errors)
    return redirect('details', product_id)


def add_order(request, product_id):
    order = Order.objects.create(
        item = Product.objects.get(id=product_id),
        user = request.user,
        date = timezone.now()
    )
    order.save()
    return redirect('details', product_id)

def delete_order(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    if order.user != request.user:
        return HttpResponseForbidden("this order cannot be deleted")
    order.delete()
    user = request.user
    UserOrders = Order.objects.filter(user=user).select_related('item')
    return redirect('order_list')


@login_required
def order_list(request):
    user = request.user
    UserOrders = Order.objects.filter(user=user).select_related('item')

    return render(request,'Order_List.html', {'orders': UserOrders},)