# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
import urllib.parse as Urllib
from scrapy.linkextractors import LinkExtractor

class PsutcrawlSpider(scrapy.Spider):
    name = "psutcrawl"
    allowed_domains = ["psut.edu.jo"]
    start_urls = ['http://psut.edu.jo/']

    def parse(self, response):
        body =response.body
        print(response.url)
        selector = Selector(text=body)

        links= (selector.xpath("//a/@href").extract())
        parsed_links = []

        clear_text=selector.xpath('//body//text()').extract()
        unique_set=(list(set(clear_text)))
        words_count={}
        for phrase  in unique_set:
            splitted = re.compile(r'\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\_|\.|\+|\-|\:|\/|\\|\n|\ ').split(phrase)
            if  splitted == []:
                continue
            else:
                print(splitted)





        for link in links:
            parsed_links.append(Urllib.urljoin(response.url,link))


        for link in parsed_links:
            pass


