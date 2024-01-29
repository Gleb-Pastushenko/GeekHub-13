from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from products_app.models import Product


@login_required()
def cart(request):
    cart = request.session.get('cart') or {}
    print(cart)
    products = []

    if cart:
        for product_id, qty in cart.items():
            if product := Product.objects.filter(pk=product_id).first():
                products.append({**model_to_dict(product), "qty": qty})

    return render(request, "cart.html", {'products': products})


@login_required()
def add_product(request, product_id):
    cart = request.session.get('cart') or {}

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect(reverse('products_app:products'))


@login_required()
def remove_product(request, product_id):
    cart = request.session.get('cart')
    cart.pop(product_id)
    request.session['cart'] = cart
    request.session.modified = True

    if cart:
        return redirect(reverse('cart_app:cart'))
    else:
        return redirect(reverse('products_app:products'))


@login_required()
def inc_product(request, product_id):
    cart = request.session.get('cart')
    cart[product_id] += 1
    request.session['cart'] = cart
    request.session.modified = True

    return redirect(reverse('cart_app:cart'))


@login_required()
def dec_product(request, product_id):
    cart = request.session.get('cart')

    if cart[product_id] > 1:
        cart[product_id] -= 1
    else:
        cart.pop(product_id)

    request.session['cart'] = cart
    request.session.modified = True

    if cart:
        return redirect(reverse('cart_app:cart'))
    else:
        return redirect(reverse('products_app:products'))


@login_required()
def clear(request):
    cart = request.session.get('cart')
    if cart:
        cart.clear()
        request.session['cart'] = cart
        request.session.modified = True

    return redirect(reverse('products_app:products'))


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = request.session.get('cart') or {}
        return Response(cart)

    def post(self, request, *args, **kwargs):
        product_id = request.data['product_id']
        qty = max(0, int(request.data['qty']))

        cart = request.session.get('cart') or {}
        cart[product_id] = qty
        request.session['cart'] = cart
        request.modified = True

        return Response(cart)

    def delete(self, request, pk, *args, **kwargs):
        cart = request.session.get('cart') or {}
        if cart.get(pk):
            cart.pop(pk)
            request.session['cart'] = cart
            request.modified = True

        return Response(cart)
