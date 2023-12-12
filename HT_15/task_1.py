# 1. Викорисовуючи requests, написати скрипт, який буде приймати на вхід ID категорії із сайту https://www.sears.com
# і буде збирати всі товари із цієї категорії, збирати по ним всі можливі дані (бренд, категорія, модель, ціна, рейтинг тощо)
# і зберігати їх у CSV файл (наприклад, якщо категорія має ID 12345, то файл буде називатись 12345_products.csv)
# Наприклад, категорія https://www.sears.com/tools-tool-storage/b-1025184 має ІД 1025184

import requests
import csv
from time import sleep
import random

HEADERS = {
    'authority': 'www.sears.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uk;q=0.6',
    'authorization': 'SEARS',
    'content-type': 'application/json',
    'referer': 'https://www.sears.com/tools-tool-storage/b-1025184',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

FIELD_NAMES = (
    'id',
    'brandName',
    'name',
    'partNum',
    'regularPrice',
    'discountPrice',
    'rating',
)


def get_group_id():
    group_id = None
    
    while not group_id:        
        try:
            group_id = int(input("Enter group id: "))
            
            if group_id < 0:
                raise ValueError("Value can't be negative!")
        
        except ValueError as error:
            print(error)
            group_id = None
    
    return group_id


def get_response(start_index, end_index, cat_group_id):
    response = requests.request(
        'get',
        'https://www.sears.com/api/sal/v3/products/search' +
        f'?startIndex={start_index}' +
        f'&endIndex={end_index}' +
        '&storeId=10153' +
        f'&catGroupId={cat_group_id}',
        headers=HEADERS,
    )
        
    return response


def write_to_csv(cat_group_id, items):
    file_name = f"{cat_group_id}_products.csv"
    
    with open(file_name, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        writer.writerows(items)


def parse_items(cat_group_id):
    start_index = 1
    end_index = 48
    offset = 48
    items = []
    
    while True:
        try:
            response = get_response(start_index, end_index, cat_group_id)
            print(f"Response status code: {response.status_code}")
            
            if response.status_code == 429:
                print("Too much requests, need to wait 60 seconds")
                sleep(60)
                continue
                
            items_list = response.json()["items"]
            items = [{
                'id': item['additionalAttributes']['id'],
                'brandName': item['brandName'],
                'name': item['name'],
                'partNum': item['partNum'],
                'regularPrice': item['price']['regularPrice'],
                'discountPrice': item['price']['finalPrice'],
                'rating': item['additionalAttributes']['rating'],                
            } for item in items_list]
            
            write_to_csv(cat_group_id, items)            
            print(f"Items {start_index} - {end_index} parsed successfully")
          
            sleep(random.randrange(15, 20))
            start_index += offset
            end_index += offset
            
        except Exception as err:
            print(err)
            print("No more elements in cathegory! Parsing complete.")
            return
            
        
if __name__ == "__main__":
    parse_items(get_group_id())
