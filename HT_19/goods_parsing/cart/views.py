from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from parse.models import Product


def cart(request):
    cart = request.session.get('cart') or {}
    print(cart)
    products = []
    
    if cart:
        for product_id, qty in cart.items():
            products.append({**(Product.objects.filter(pk=product_id).values()[0]), "qty": qty})

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
