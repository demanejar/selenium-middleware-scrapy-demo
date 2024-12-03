import scrapy


class VinpearlDotComSpider(scrapy.Spider):
    name = "vinpearl_dot_com"
    allowed_domains = ["vinpearl.com"]
    start_urls = ["https://vinpearl.com/vi/news/ha-noi"]

    def parse(self, response):
        pass
