import scrapy
from seleniummiddlewarescrapydemo.items import SeleniummiddlewarescrapydemoItem

class VinpearlDotComSpider(scrapy.Spider):
    name = "vinpearl_dot_com"
    allowed_domains = ["vinpearl.com"]
    start_urls = ["https://vinpearl.com/vi/news/ha-noi"]

    def parse(self, response):
        # scroll to end
        driver = response.request.meta["driver"]
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )


        contents = response.css('.view-content .news-item')
        
        for content in contents:
            url = content.css('a').xpath('./@href').get()

            item = SeleniummiddlewarescrapydemoItem()
            item['url'] = url

            yield item
