# -*- coding: utf-8 -*-
import scrapy
import redis

import re
from scrapy.selector import Selector
import urllib.parse as Urllib
from PsutCrawler.items import PsutcrawlerItem
from scrapy.linkextractors import LinkExtractor

class PsutcrawlSpider(scrapy.Spider):
    name = "psutcrawl"
    allowed_domains = ["luaybs.com/"]
    start_urls = ['http://www.luaybs.com/']

    def parse(self, response):
        words_count={}
        body =response.body
        print(response.url)
        selector = Selector(text=body)

        links= (selector.xpath("//a/@href").extract())
        parsed_links = []

        clear_text=selector.xpath('//body//text()').extract()
        unique_set=(list(set(clear_text)))
        for phrase  in unique_set:
            splitted = re.compile \
                (r"""\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\.+|\+|\-|\:|\/|\\|\n+|\r+|\ +|\t+|\,+|[0-9]*""") \
                .split(phrase)
            for split in splitted:
                if  split in[[],'\n','',""]:
                    continue
                else:
                    if split in list(words_count.keys()):
                        words_count[str(split)]=words_count[split]+1
                    else:
                        words_count[str(split)] = 1

        item=PsutcrawlerItem()
        item['values']=words_count
        yield item
        for link in links:
            parsed_links.append(Urllib.urljoin(response.url,link))


        for link in parsed_links:
            yield scrapy.Request(link,callback=self.parse)


