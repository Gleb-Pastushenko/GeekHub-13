from typing import Any, Iterable
import scrapy
from bs4 import BeautifulSoup
import csv

class ExtentionsSpider(scrapy.Spider):
    name = "extentions"

    start_urls = ["https://chrome.google.com/webstore/sitemap"]
    
    def parse(self, response):            
        urls = self.get_loc_urls(response)
        
        for url in urls:
            yield scrapy.Request(url, self.parse_exts_urls)

    def parse_exts_urls(self, response):
        urls = self.get_exts_urls(response)

        for url in urls:
            yield scrapy.Request(url, self.parse_ext_page)

    def parse_ext_page(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        id = response.url.split('/')[-1]
        name = response.css("meta[property=\"og:title\"]::attr(content)").get()
        description = response.css("meta[property=\"og:description\"]::attr(content)").get()

        self.write_to_csv({"id": id, "name": name, "description": description})

    def get_loc_urls(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        urls = [item.get_text() for item in soup.select('loc')]
        return urls
    
    def get_exts_urls(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        urls = [item.get_text() for item in soup.select('loc')]
        return urls
    
    def write_to_csv(self, ext_info):
        try:
            with open('extensions.csv', 'a', newline='', encoding='utf-8') as file:
                fieldnames = ('id', 'name', 'description')
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(ext_info)
        except:
            with open('extensions.csv', 'w', newline='', encoding='utf-8') as file:
                fieldnames = ('id', 'name', 'description')
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(ext_info)