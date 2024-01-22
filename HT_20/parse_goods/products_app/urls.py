from django.urls import path

from products_app import views

app_name = 'products_app'

urlpatterns = [
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('products/cat/<category>', views.ProductsListByCategoryView.as_view(), name='products_by_category'),
    path('product/<pk>', views.ProductDetailView.as_view(), name='product_details'),
    path('product/edit/<pk>', views.ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<pk>', views.ProductDeleteView.as_view(), name='delete_product'),
    path('parse/', views.ParseFormView.as_view(), name='parse'),
]