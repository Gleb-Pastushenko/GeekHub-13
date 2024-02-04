from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('auth_app.urls')),
    path('', include('products_app.urls')),
    path('cart/', include('cart_app.urls')),
]
