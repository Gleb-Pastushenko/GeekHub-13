from django.urls import path

from . import views

app_name = "parse"

urlpatterns = [
    path("", views.EnterIdsFormView.as_view(), name="add_products"),
    path("my_products/", views.MyProductsView.as_view(), name="my_products"),
    path("product/<pk>/", views.ProductView.as_view(), name="product"),
]
