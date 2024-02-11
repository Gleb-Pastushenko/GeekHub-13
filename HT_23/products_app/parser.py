from time import sleep

import requests

from .models import Product

HEADERS = {
    'authority': 'www.sears.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uk;q=0.6',
    'authorization': 'SEARS',
    'content-type': 'application/json',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}


class Parser:
    def __init__(self, id_list):
        self.id_list = id_list

    def get_response_json(self, product_id):
        tries = 10

        while tries:
            tries -= 1

            try:
                params = {
                    'storeName': 'Sears',
                    'memberStatus': 'G',
                    'zipCode': '10101',
                }

                response = requests.get(
                    f'https://www.sears.com/api/sal/v3/products/details/{product_id}',
                    params=params,
                    headers=HEADERS,
                )

                return response.json()

            except requests.JSONDecodeError:
                sleep(10)

        raise Exception(
            "Unsuccessful product data request 10 times in a row. Requests terminated")

    def get_product_data(self, product_id):
        try:
            print(f"PRODUCT ID: {product_id}")
            response_json = self.get_response_json(product_id)
            product_data = response_json['productDetail']['softhardProductdetails'][0]
            product = {
                'id': product_data['identity']['sSin'],
                'name': product_data['descriptionName'],
                'brand_name': product_data['brandName'],
                'price': product_data['regularPrice'],
                'description': product_data['shortDescription'],
                'category': product_data['hierarchies']['specificHierarchy'][-1]['name'],
                'link': product_data['seoUrl'],
            }

        except Exception as err:
            print(
                f"The next error occurs while parsing the product data: \n{err}")
            product = None

        return product

    def run(self):
        for product_id in self.id_list:
            product = self.get_product_data(product_id)
            if product is not None:
                Product.objects.update_or_create(
                    id=product_id, defaults=product)
