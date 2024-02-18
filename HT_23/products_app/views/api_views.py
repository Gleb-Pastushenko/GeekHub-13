import subprocess
from sys import stdout, stdin, stderr
from pathlib import Path

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from products_app.serializers import ProductsSerializer
from products_app.models import Product


class ProductsAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        else:
            return [IsAdminUser()]


class ProductAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        else:
            return [IsAdminUser()]


class ProductsParseAPIView(APIView):
    def get_permissions(self):
        return [IsAdminUser()]

    def post(self, request):
        self.start_subprocess(request.data)
        return Response(request.data.get('id_list'))

    def start_subprocess(self, id_list):
        project_root = Path(__file__).parent.parent.parent
        manage_py_path = Path(project_root, "manage.py")
        command = f'python {manage_py_path} shell --command="from products_app.parser import Parser; Parser({id_list}).run()"'
        subprocess.Popen(command, shell=True, stdin=stdin,
                         stdout=stdout, stderr=stderr)
