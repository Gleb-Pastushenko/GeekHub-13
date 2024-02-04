from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from auth_app.forms import LoginForm


def user_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('products_app:products')

    context = {'form': form}

    return render(request, 'auth.html', context)


def user_logout(request):
    logout(request)
    return redirect('products_app:products')
