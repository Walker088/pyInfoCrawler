# -*- coding: utf-8 -*-
import scrapy
from crawler.items import InfocasaItem

class InfocasaSpider(scrapy.Spider):
    #root_url = 'https://www.infocasas.com.py'
    name = 'infocasas.com.py'
    allowed_domains = ['infocasas.com.py']
    start_urls = ['https://www.infocasas.com.py/alquiler']

    def parseEstate(self, response):
        import re
        self.logger.debug('parseEstate id: %s', re.sub('[^\d]+', '', response.url.split('/')[-1]))
        try:
            price = response.xpath('//p[@class="precio-final"]//text()').get()
            estate = InfocasaItem()
            estate['propertyId'] = re.sub('[^\d]+', '', response.url.split('/')[-1])
            estate['propertyName'] = response.xpath('//h1//text()').get()
            estate['propertyLocation'] = response.xpath('//div[@class="ficha-tecnica"]//p[text()[contains(., "Zona")]]//following::div//text()').get()
            estate['corruncyName'] = price.split(' ')[0]
            estate['propertyPrice'] = price.split(' ')[1]
            estate['numberOfRoom'] = response.xpath('//div[@class="ficha-tecnica"]//p[text()[contains(., "Dormitorios")]]//following::div//text()').get()
            estate['numberOfBath'] = response.xpath('//div[@class="ficha-tecnica"]//p[text()[contains(., "Baño")]]//following::div//text()').get()
            estate['propertyType'] = response.xpath('//div[@class="ficha-tecnica"]//p[text()[contains(., "Tipo Propiedad")]]//following::div//text()').get()
            estate['propertyState'] = response.xpath('//div[@class="ficha-tecnica"]//p[text()[contains(., "Estado")]]//following::div//text()').get()
            estate['buildYear'] = response.xpath('//div[@class="ficha-tecnica"]//p[text()[contains(., "construcción:")]]//following::div//text()').get()
            estate['squareMeter'] = response.xpath('//div[@class="ficha-tecnica"]//p[text()[contains(., "edificados")]]//following::div//text()').get()
            yield estate
        except Exception as e:
            self.logger.error(e)

    def parse(self, response):
        #self.logger.debug('A response from %s just arrived!', response.url)
        for prop in response.xpath('//div[contains(@class, "propiedades-slider")]//a[@class="checkMob"]//@href').getall():
            yield scrapy.Request(url=response.urljoin(prop), callback=self.parseEstate)

        next_page = response.xpath('//div[@id="paginado"]//a[contains(@class, "next")]//@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
