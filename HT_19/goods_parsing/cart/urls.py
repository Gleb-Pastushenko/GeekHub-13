from django.urls import path

from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart, name="cart"),
    path("add_product/<product_id>", views.add_product, name="add_product"),
    path("remove_product/<product_id>", views.remove_product, name="remove_product"),
    path("clear_cart/", views.clear_cart, name="clear_cart"),
    path("product_inc/<product_id>", views.product_inc, name="product_inc"),
    path("product_dec/<product_id>", views.product_dec, name="product_dec"),


    # path("parse/", views.EnterIdsFormView.as_view(), name="parse"),
    # path("products/", views.ProductsListView.as_view(), name="products"),
    # path("product/<pk>", views.ProductDetailView.as_view(), name="product_details"),    
]