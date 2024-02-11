from django.urls import path

from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]
