from rest_framework.serializers import ModelSerializer

from products_app.models import Product


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'brand_name', 'price',
                  'description', 'link', 'category']
