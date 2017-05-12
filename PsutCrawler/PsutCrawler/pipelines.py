# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
class PsutcrawlerPipeline(object):
    connection=None
    def __init__(self):
        print("trying to connect to redis database")
        try:
            self.connection = redis.Redis(host='localhost')
        except Exception as redis_excpetion:
            print ("something crashed")
            print(str(redis_excpetion))

    def process_item(self, item, spider):
        print ("testing connections")
        for i in item['values'].keys():
            if self.connection.get(i)==None:
                self.connection.set(i,item['values'][i])
            else:
                self.connection.set(i, item['values'][i]+int(self.connection.get(i)))

        return item
