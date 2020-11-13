from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from .models import *
from django.contrib import messages
from django.db.models import Count
from django.db.models import Sum
from django.core.mail import send_mail



def index(request):
    context = {
    "time": strftime("%b %d, %Y  %H:%M %p", gmtime())
    }
    return render(request, "index.html", context)

def services(request):
    context = {
    "time": strftime("%b %d, %Y  %H:%M %p", gmtime())
    }
    return render(request, "services.html", context)

def aboutus(request):
    context = {
    "time": strftime("%b %d, %Y  %H:%M %p", gmtime())
    }
    return render(request, "aboutus.html", context)

def contactus(request):
    context = {
    "time": strftime("%b %d, %Y  %H:%M %p", gmtime())
    }
    return render(request, "contactus.html", context)

def regpage(request):
    context = {
    "time": strftime("%b %d, %Y  %H:%M %p", gmtime())
    }
    return render(request, "Registeration.html", context)


def register(request):
    if request.method == "GET":
        return redirect("/")
    errors = User.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/regpage')
    else:
        new_user = User.objects.register(request.POST)
        new_cart = cart.objects.create(user = new_user)
        request.session['user_id'] = new_user.id
        request.session['cart_id'] = new_cart.id
        return redirect('/orders')


def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user1 = User.objects.get(email=request.POST['email'])
    cart1 = cart.objects.get(user=user1)
    request.session['user_id'] = user1.id
    request.session['cart_id'] = cart1.id
    return redirect('/orders')

def logout(request):
    request.session.clear()
    return redirect('/')


def inquiry(request):
    errors = Inquiry.objects.validatornew(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        new_inquiry = Inquiry.objects.add(request.POST)
        send_mail('TestingInquiry', 'Thank you for your inquiry. Someone from our customer service will be getting in touch with you soon', 'noreply@noreply.com', ['imran_khan2888@hotmail.com',])
        return redirect('/')


def orders(request):
    user1 = User.objects.get(id=request.session['user_id'])
    cart1 = cart.objects.get(id=request.session['cart_id'])
    full_price = cart1.total_price
    cart1_quantity = cart1.quantity
    context = {
        'user': user1,
        "user_cart": cart1,
        "all_products": Product.objects.all(),
        "total_price": full_price,
        "cart1_quantity": cart1_quantity,
        
    }
    return render(request, 'orders.html', context)

def cartadd(request, product_id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == 'POST':
        user = User.objects.get(id=request.session['user_id'])
        cart1 = cart.objects.get(id=request.session['cart_id'])
        product = Product.objects.get(id=product_id)
        check_product_exists = cart1.product.filter(id=product_id)
        if check_product_exists:
             return redirect('/orders')
        else:
            product.products_added_carts.add(cart1)
            cart1.total_price = cart1.total_price + product.price
            # cart1.quantity = (request.POST["hours"])
            cart1.quantity = cart1.quantity + 1
            # cart1.save()
            cart1.save()
            
    return redirect('/orders')
    
def cartdelete(request, item_id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    cart1 = cart.objects.get(id=request.session['cart_id'])
    product = Product.objects.get(id=item_id)
    product.products_added_carts.remove(cart1)
    cart1.total_price = cart1.total_price - product.price
    cart1.quantity = cart1.quantity - 1
    cart1.save()
    return redirect('/orders')
    



def purchase(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == 'POST':
        this_product = Product.objects.filter(id=request.POST["id"])
        if not this_product:
            return redirect('/')
        else:
            quantity = int(request.POST["quantity"])
            total_charge = quantity*(float(this_product[0].price))
            Order.objects.create(quantity_ordered=quantity, total_price=total_charge)
            return redirect('/checkout')
    else:
        return redirect('/')

def checkout(request):
    if 'user_id' not in request.session:
        return redirect('/')
    last = Order.objects.last()
    price=last.total_price
    full_order = Order.objects.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum']
    full_price = Order.objects.aggregate(Sum('total_price'))['total_price__sum']
    context = {
        'orders':full_order,
        'total':full_price,
        'bill':price,
    }
    return render(request, "checkout.html",context)




