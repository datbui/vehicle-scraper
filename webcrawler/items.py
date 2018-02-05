# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Vehicle(scrapy.Item):
    name = scrapy.Field()
    make = scrapy.Field()
    model = scrapy.Field()
    modification = scrapy.Field()
    vin = scrapy.Field()
    price = scrapy.Field()
    mileage = scrapy.Field()
    year = scrapy.Field()
    mpg = scrapy.Field()
    engine = scrapy.Field()
    fuel = scrapy.Field()
    drive = scrapy.Field()
    transmission = scrapy.Field()
    interior = scrapy.Field()
    exterior = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()
