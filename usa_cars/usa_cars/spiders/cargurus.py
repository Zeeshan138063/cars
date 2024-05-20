import scrapy


class CargurusSpider(scrapy.Spider):
    name = "cargurus"
    allowed_domains = ["www.cargurus.ca"]
    start_urls = ["https://www.cargurus.ca/Cars/l-Used-Chevrolet-m1"]

    def parse(self, response):
        pass
