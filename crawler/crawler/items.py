# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InfocasaItem(scrapy.Item):
    propertyId       = scrapy.Field()
    propertyName     = scrapy.Field()
    propertyLocation = scrapy.Field()
    propertyPrice    = scrapy.Field()
    corruncyName     = scrapy.Field()
    numberOfRoom     = scrapy.Field()
    numberOfBath     = scrapy.Field()
    propertyType     = scrapy.Field()
    propertyState    = scrapy.Field()
    buildYear        = scrapy.Field()
    squareMeter      = scrapy.Field()
