import scrapy


class SearchSpider(scrapy.Spider):
    name = 'search'

    def start_requests(self):
        url = 'http://www.gofundme.com/s?q=' + self.q
        yield scrapy.Request(url=url)

    def parse(self, response):
        print(response)
