# -*- coding: utf-8 -*-
import scrapy


class PsutSpider(scrapy.Spider):
    name = "psut"
    allowed_domains = ["psut.edu.jo"]
    start_urls = ['http://psut.edu.jo/']

    def parse(self, response):
        print (response.body)
