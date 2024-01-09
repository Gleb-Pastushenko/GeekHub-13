from datetime import timezone
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

    def get_response_json(self, id):
        while True:
            try:
                params = {
                    'storeName': 'Sears',
                    'memberStatus': 'G',
                    'zipCode': '10101',
                }

                response = requests.get(
                    f'https://www.sears.com/api/sal/v3/products/details/{id}',
                    params=params,
                    headers=HEADERS,
                )

                return response.json()
            
            except requests.JSONDecodeError:
                sleep(10)

    def get_product_data(self, id):
        response_json = self.get_response_json(id)
        try:
            product_data = response_json['productDetail']['softhardProductdetails'][0]
            product = {'id': id,
                       'name': product_data['descriptionName'],
                       'brand_name': product_data['brandName'],
                       'regular_price': product_data['price']['finalPrice'],
                       'description': product_data['shortDescription'],                       
                       'link': 'https://www.sears.com' + product_data['seoUrl'],
                       }          
        except Exception:
            product = None
        return product

    def run(self):
        for id in self.id_list:
            product = self.get_product_data(id)
            if product is not None:
                Product.objects.update_or_create(
                    id=id, defaults=product)
