# 3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
#    цитата, автор, інфа про автора тощо.
# - збирається інформація з 10 сторінок сайту.
# - зберігати зібрані дані у CSV файл


import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "http://quotes.toscrape.com"


def parse_page(response, quotes_list):
    quotes_page = BeautifulSoup(response.text, 'lxml')
    quotes = quotes_page.select("div.quote")

    for quote in quotes:
        about_link = BASE_URL + quote.select_one("small + a").attrs['href']
        about_response = requests.get(about_link)
        about_bs = BeautifulSoup(about_response.text, 'lxml')
        birth_date = about_bs.select_one(".author-born-date").text
        birth_location = about_bs.select_one(".author-born-location").text[3:]

        quotes_list.append(
            {
                "text": quote.select_one(".text").text.strip("“”"),
                "author_name": quote.select_one("small.author").text,
                "author_birth_date": birth_date,
                "author_birth_location": birth_location,
                "tags": [tag.text for tag in quote.select("a.tag")]
            }
        )
    return not quotes_page.select_one("ul.pager .next")


if __name__ == "__main__":
    quotes_list = []
    page = 0
    last = False

    while not last:
        page += 1
        response = requests.get(f"http://quotes.toscrape.com/page/{page}")
        last = parse_page(response, quotes_list)

    print(f"{page} pages have been parsed")

    with open('quotes.csv', 'w', encoding="utf-8") as file:
        csv_writer = csv.DictWriter(file, fieldnames=[
                                    "text", "author_name", "author_birth_date", "author_birth_location", "tags"])
        csv_writer.writeheader()
        csv_writer.writerows(quotes_list)
