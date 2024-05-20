from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.auto_canada import AutoCanadaSpider
from spiders.cargurus import CargurusSpider
from spiders.kijiji import KijijiSpider


def trigger_process():
    spiders = [AutoCanadaSpider]#, KijijiSpider, CargurusSpider]
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    # Define the arguments to be passed
    for spider in spiders:
        process.crawl(spider, **{})
    process.start()  # the script will block here until all crawling jobs are finished


if __name__ == '__main__':
    trigger_process()