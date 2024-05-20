import scrapy


class KijijiSpider(scrapy.Spider):
    name = "kijiji"
    allowed_domains = ["www.kijijiautos.ca"]
    start_urls = ["https://www.kijijiautos.ca/cars/"]

    def parse(self, response):
        pass
