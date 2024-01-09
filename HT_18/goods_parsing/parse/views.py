import subprocess
from sys import stdout, stdin, stderr
from pathlib import Path

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import FormView

from .models import Product
from .forms import EnterIdsForm


class EnterIdsFormView(FormView):
    template_name = 'parse/index.html'
    form_class = EnterIdsForm

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

        return render(request, 'parse/index.html', context=context)

    def start_subprocess(self, id_list):
        project_root = Path(__file__).parent.parent
        manage_py_path = Path(project_root, "manage.py")
        command = f'python {manage_py_path} shell --command="from parse.parser import Parser; Parser({id_list}).run()"'
        process = subprocess.Popen(
            command, shell=True, stdin=stdin, stdout=stdout, stderr=stderr)


class ProductsListView(ListView):
    model = Product
    template_name = "parse/my_products.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "parse/product.html"
    context_object_name = "product"
