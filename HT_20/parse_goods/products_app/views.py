import subprocess
from sys import stdout, stdin, stderr
from pathlib import Path

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

from products_app.models import Product
from products_app.forms import EnterIdsForm


class ProductsListView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = set(Product.objects.values_list('category',flat=True))
        context['categories'] = categories

        return context
    

class ProductsListByCategoryView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"

    def get_queryset(self):
        category = self.kwargs.get('category')
        return Product.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs.get('category')
        context['categories'] = [category]

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "product"


class ParseFormView(UserPassesTestMixin, FormView):
    template_name = 'parse.html'
    form_class = EnterIdsForm

    def test_func(self):
        return self.request.user.is_superuser
    
    def post(self, request, *args, **kwargs):
        form = EnterIdsForm(request.POST)
        context = {'form': EnterIdsForm()}

        if form.is_valid():
            id_list = form.cleaned_data['id_list'].split(',')
            id_list = set(item.strip() for item in id_list)
            self.start_subprocess(id_list)

            context.update({'message': 'Products scraping start successfully'})
        else:
            context.update({'message': 'Form data unsuccessfully'})

        return render(request, 'parse.html', context=context)

    def start_subprocess(self, id_list):
        project_root = Path(__file__).parent.parent
        manage_py_path = Path(project_root, "manage.py")
        command = f'python {manage_py_path} shell --command="from products_app.parser import Parser; Parser({id_list}).run()"'
        subprocess.Popen(command, shell=True, stdin=stdin, stdout=stdout, stderr=stderr)


def is_superuser(user):
    return user.is_superuser


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'edit_product.html'
    fields = ['id', 'name', 'brand_name', 'price', 'description', 'link', 'category']
    success_url = reverse_lazy('products_app:products')

    def test_func(self):
            return self.request.user.is_superuser


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('products_app:products')

    def test_func(self):
        return self.request.user.is_superuser
