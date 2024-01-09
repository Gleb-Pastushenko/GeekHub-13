from django.urls import path

from . import views

app_name = "parse"

urlpatterns = [
    path("parse/", views.EnterIdsFormView.as_view(), name="parse"),
    path("", views.MyProductsView.as_view(), name="products"),
    path("<pk>/", views.ProductView.as_view(), name="product_details"),
]
