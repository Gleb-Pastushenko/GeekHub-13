# 2. Викорисовуючи requests, заходите на ось цей сайт "https://www.expireddomains.net/deleted-domains/" (з ним будьте обережні),
# вибираєте будь-яку на ваш вибір доменну зону і парсите список  доменів - їх там буде десятки тисяч (звичайно ураховуючи пагінацію).
# Всі отримані значення зберігти в CSV файл.

import csv
import random
from time import sleep

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


BASE_URL = "https://www.expireddomains.net/deleted-domains/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


def get_response(url):
    try:
        response = requests.request(method='get', url=url, headers={
                                    'User-Agent': USER_AGENT})
        response.raise_for_status()
        return response
    except Exception:
        return None


def next_page_url(response):
    try:
        soup = BeautifulSoup(response.text, "lxml")
        url = soup.select_one("a.next").get("href")
        return urljoin(BASE_URL, url)
    except Exception:
        print("No more pages available!")
        return None


def get_domains(response):
    soup = BeautifulSoup(response.text, "lxml")
    return [[element.text] for element in soup.select("a.namelinks")]


def parse_domains():
    domains = []
    url = BASE_URL

    while url:
        sleep(random.randint(5, 10))
        response = get_response(url)
        save_to_csv(get_domains(response))
        print(f"Domains parsed from: {url}")
        url = next_page_url(response)
        print(f"Next url: {url}")

    return domains


def save_to_csv(domains):
    with open("domains.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerows(domains)


if __name__ == "__main__":
    parse_domains()
