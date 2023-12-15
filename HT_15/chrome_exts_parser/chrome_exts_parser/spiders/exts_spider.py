import csv

from bs4 import BeautifulSoup
import scrapy

from chrome_exts_parser.items import ChromeExtsParserItem


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
        item = ChromeExtsParserItem()

        item['id'] = response.url.split('/')[-1]
        item['name'] = response.css("meta[property=\"og:title\"]::attr(content)").get()
        item['description'] = response.css("meta[property=\"og:description\"]::attr(content)").get()

        yield item        

    def get_loc_urls(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        urls = [item.get_text() for item in soup.select('loc')]
        return urls
    
    def get_exts_urls(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        urls = [item.get_text() for item in soup.select('loc')]
        return urls
    