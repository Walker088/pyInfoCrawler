# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InfocasaItem(scrapy.Item):
    propertyId       = scrapy.Field()
    propertyName     = scrapy.Field()
    department       = scrapy.Field()
    district         = scrapy.Field()
    propertyPrice    = scrapy.Field()
    currencyName     = scrapy.Field()
    numberOfRoom     = scrapy.Field()
    numberOfBath     = scrapy.Field()
    propertyType     = scrapy.Field()
    propertyState    = scrapy.Field()
    buildYear        = scrapy.Field()
    squareMeter      = scrapy.Field()
    url              = scrapy.Field()

class InfocasaDepartmentItem(scrapy.Item):
    departmentId = scrapy.Field()
    departmentName = scrapy.Field()
    infocasaCountryId = scrapy.Field()
    infocasaDepId = scrapy.Field()