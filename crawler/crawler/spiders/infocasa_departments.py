# -*- coding: utf-8 -*-

import scrapy
import json

from crawler.items import InfocasaDepartmentItem

class InfocasaDepartment(scrapy.Spider):
    name = 'departments.infocasas.com.py'
    allowed_domains = ['infocasas.com.py']
    start_urls = ['https://www.infocasas.com.py']
    custom_settings = {
        'ITEM_PIPELINES': {
            'crawler.pipelines.InfoCasaRegions': 100,
        }
    }

    def parseDepartamento(self, response):
        try:
            deps = json.loads(response.text)
            #self.logger.debug(deps)
            for dep in deps:
                item = InfocasaDepartmentItem()
                item['infocasaCountryId'] = dep['IDpais']
                item['infocasaDepId'] = dep['id']
                item['departmentName'] = dep['nombre']
                yield item
        except Exception as e:
            self.logger.error(e)

    def parse(self, response):
        query = '/?mid=ubications&func=ajax_departamentosPais&IDpais=2'
        yield scrapy.Request(url=response.urljoin(query), callback=self.parseDepartamento)
