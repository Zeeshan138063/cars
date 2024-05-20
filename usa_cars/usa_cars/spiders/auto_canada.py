import scrapy


class AutoCanadaSpider(scrapy.Spider):
    name = "auto_canada"
    allowed_domains = ["www.autocan.ca"]
    start_urls = ["https://www.autocan.ca/"]

    def parse(self, response):
        pass
