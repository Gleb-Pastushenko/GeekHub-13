from unittest.mock import patch
from pathlib import Path

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

from .models import Product
from .serializers import ProductsSerializer


class ProductsAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.products_url = '/api/products/' 
        self.user = User.objects.create_user(username='user', password='password')
        self.admin_user = User.objects.create_user(username='admin', password='admin_password', is_staff=True)

    def test_get_products(self):
        
        product1 = Product.objects.create(
            id='prod_id_1',
            name='Product 1',
            brand_name='prod_brand_1',
            price=10.10,
            description='description',
            link='http://product.test',
            category='category_1'
        )

        product2 = Product.objects.create(
            id='prod_id_2',
            name='Product 2',
            brand_name='prod_brand_2',
            price=20.20,
            description='description',
            link='http://product.test',
            category='category_2'
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.products_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]['id'], 'prod_id_1')
        self.assertEqual(response.data[0]['name'], 'Product 1')
        self.assertEqual(response.data[0]['brand_name'], 'prod_brand_1')
        self.assertEqual(float(response.data[0]['price']), 10.1)
        self.assertEqual(response.data[0]['description'], 'description')
        self.assertEqual(response.data[0]['link'], 'http://product.test')
        self.assertEqual(response.data[0]['category'], 'category_1')

        self.assertEqual(response.data[1]['id'], 'prod_id_2')
        self.assertEqual(response.data[1]['name'], 'Product 2')
        self.assertEqual(response.data[1]['brand_name'], 'prod_brand_2')
        self.assertEqual(float(response.data[1]['price']), 20.2)
        self.assertEqual(response.data[1]['description'], 'description')
        self.assertEqual(response.data[1]['link'], 'http://product.test')
        self.assertEqual(response.data[1]['category'], 'category_2')

    def test_create_product_as_admin(self):
        self.client.force_authenticate(user=self.admin_user)

        data = {
            'id':'product_id_admin',
            'name': 'Admin Product',
            'brand_name': 'admin_brand',
            'price': 30.3,
            'description': 'admin_description',
            'link': 'http://admin_product.test',
            'category': 'admin_category'
        }

        response = self.client.post(self.products_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

        self.assertEqual(response.data['id'], 'product_id_admin')
        self.assertEqual(response.data['name'], 'Admin Product')
        self.assertEqual(response.data['brand_name'], 'admin_brand')
        self.assertEqual(float(response.data['price']), 30.3)
        self.assertEqual(response.data['description'], 'admin_description')
        self.assertEqual(response.data['link'], 'http://admin_product.test')
        self.assertEqual(response.data['category'], 'admin_category')

    def test_create_product_as_regular_user(self):        
        self.client.force_authenticate(user=self.user)

        data = {'id': 'prod_id_3', 'name': 'product_3', 'brand_name': 'product_brand_3', 'price': 30.3, 'description': 'product_description_3', 'link': 'http://product_3.test', 'category': 'product_category_3'}
        response = self.client.post(self.products_url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Product.objects.count(), 0)


class ProductAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.product = Product.objects.create(
            id='prod_id_1',
            name='Test Product',
            brand_name='prod_brand_1',
            price=10.10,
            description='description',
            link='http://product.test',
            category='category_1'
        )

        self.product_url = f'/api/products/{self.product.id}/'
        self.user = User.objects.create_user(username='user', password='password')
        self.admin_user = User.objects.create_user(username='admin', password='admin_password', is_staff=True)

    def test_get_product(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.product_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['id'], 'prod_id_1')
        self.assertEqual(response.data['name'], 'Test Product')
        self.assertEqual(response.data['brand_name'], 'prod_brand_1')
        self.assertEqual(float(response.data['price']), 10.1)
        self.assertEqual(response.data['description'], 'description')
        self.assertEqual(response.data['link'], 'http://product.test')
        self.assertEqual(response.data['category'], 'category_1')

    def test_update_product_as_admin(self):
        self.client.force_authenticate(user=self.admin_user)

        data = {
            'id':'prod_id_1',
            'name': 'Updated Product',
            'brand_name': 'admin_brand',
            'price': 30.3,
            'description': 'admin_description',
            'link': 'http://admin_product.test',
            'category': 'admin_category'
        }

        response = self.client.put(self.product_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')
        self.assertEqual(float(self.product.price), 30.3)

    def test_update_product_as_regular_user(self):
        self.client.force_authenticate(user=self.user)

        data = {'name': 'Updated Product', 'price': 20}
        response = self.client.put(self.product_url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(float(self.product.price), 10.10)

    def test_delete_product_as_admin(self):
        self.client.force_authenticate(user=self.admin_user)

        response = self.client.delete(self.product_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Product.DoesNotExist):
            self.product.refresh_from_db()

    def test_delete_product_as_regular_user(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(self.product_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(float(self.product.price), 10.10)


class ProductsParseAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.products_parse_url = '/api/parse/'
        self.user = User.objects.create_user(username='user', password='password')
        self.admin_user = User.objects.create_user(username='admin', password='admin_password', is_staff=True)

    def test_post_as_regular_user(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.products_parse_url, {'id_list': [1, 2, 3]})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
