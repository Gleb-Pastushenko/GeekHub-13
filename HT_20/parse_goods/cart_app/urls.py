from django.urls import path

from cart_app import views

app_name = 'cart_app'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<product_id>', views.add_product, name='add_product'),
    path('remove/<product_id>', views.remove_product, name='remove_product'),
    path('inc/<product_id>', views.inc_product, name='inc_product'),
    path('dec/<product_id>', views.dec_product, name='dec_product'),
    path('clear/', views.clear, name='clear'),
]