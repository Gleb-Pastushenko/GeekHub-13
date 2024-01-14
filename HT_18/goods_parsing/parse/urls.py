from django.urls import path

from . import views

app_name = "parse"

urlpatterns = [
    path("parse/", views.EnterIdsFormView.as_view(), name="parse"),
    path("", views.ProductsListView.as_view(), name="products"),
    path("id/<pk>/", views.ProductDetailView.as_view(), name="product_details"),
]
