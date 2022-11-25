import scrapy


class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['www.gofundme.com']
    start_urls = ['http://www.gofundme.com/']

    def parse(self, response):
        print(response)
