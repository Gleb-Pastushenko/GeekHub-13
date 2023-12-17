import csv

from bs4 import BeautifulSoup
import scrapy

from chrome_exts_parser.items import ChromeExtsParserItem


class ExtentionsSpider(scrapy.Spider):
    name = "extentions"

    start_urls = ["https://chrome.google.com/webstore/sitemap"]
    
    def parse(self, response):            
        yield from response.follow_all(xpath="//*[local-name() = 'loc']/text()", callback=self.parse_exts_urls)

    def parse_exts_urls(self, response):
        yield from response.follow_all(xpath="//*[local-name() = 'loc']/text()", callback=self.parse_ext_page)

    def parse_ext_page(self, response):
        item = ChromeExtsParserItem()

        item['id'] = response.url.split('/')[-1]
        item['name'] = response.css("meta[property=\"og:title\"]::attr(content)").get()
        item['description'] = response.css("meta[property=\"og:description\"]::attr(content)").get()

        yield item        
    