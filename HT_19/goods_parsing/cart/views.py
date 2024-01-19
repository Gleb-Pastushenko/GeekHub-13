from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import model_to_dict

from parse.models import Product


def cart(request):
    cart = request.session.get('cart') or {}
    print(cart)
    products = []
    
    if cart:
        for product_id, qty in cart.items():
            if product := Product.objects.filter(pk=product_id).first():
                products.append({**model_to_dict(Product.objects.get(pk=product_id)), "qty": qty})

    return render(request, "cart/my_products.html", {'products': products})


def add_product(request, product_id):
    cart = request.session.get('cart') or {}

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect(reverse('parse:products'))


def remove_product(request, product_id):
    cart = request.session.get('cart')
    cart.pop(product_id)
    request.session['cart'] = cart
    request.session.modified = True

    if cart:
        return redirect(reverse('cart:cart'))
    else:
        return redirect(reverse('parse:products'))
    

def clear_cart(request):
    cart = request.session.get('cart')
    if cart:            
        cart.clear()
        request.session['cart'] = cart
        request.session.modified = True

    return redirect(reverse('parse:products'))


def product_inc(request, product_id):
    cart = request.session.get('cart')
    cart[product_id] += 1
    request.session['cart'] = cart
    request.session.modified = True

    return redirect(reverse('cart:cart'))


def product_dec(request, product_id):
    cart = request.session.get('cart')

    if cart[product_id] > 1:
        cart[product_id] -= 1
    else:
        cart.pop(product_id)

    request.session['cart'] = cart
    request.session.modified = True

    if cart:
        return redirect(reverse('cart:cart'))
    else:
        return redirect(reverse('parse:products'))
