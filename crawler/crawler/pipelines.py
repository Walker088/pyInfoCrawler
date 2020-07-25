# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
# from crawler.settings import PgConfig
from crawler.settings import PgConfig

class InfocasaPipeline:
    conf = PgConfig()
    type_id = 'T01'
    crawled_id = ''
    prefix = 'C'

    def open_spider(self, spider):
        hostname = self.conf.get_host()
        username = self.conf.get_user()
        password = self.conf.get_pass()
        database = self.conf.get_db()
        port = self.conf.get_port()
        self.conn = psycopg2.connect(host=hostname, port=port, user=username, password=password, dbname=database)
        self.cur = self.conn.cursor()
        self.conn.autocommit = True

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        if '' == InfocasaPipeline.crawled_id:
            InfocasaPipeline.crawled_id = self.get_crawled_id()
            sql = 'INSERT INTO public.crawled_records(crawled_id, crawled_date, source_type, crawled_at) VALUES (%s, current_date, %s, current_timestamp)'
            self.cur.execute(sql, (InfocasaPipeline.crawled_id, InfocasaPipeline.type_id))
        department_id = self.get_department_id(item['department'])
        district_id = self.get_district_id(department_id, item['district'])
        sql  = 'INSERT INTO public.infocasa_alquiler(crawled_id, property_id, property_name, department_id, district_id, price, currency, nroom, nbath, property_type, property_state, build_at, area_meter, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        self.cur.execute(sql, (InfocasaPipeline.crawled_id, item['propertyId'], item['propertyName'], department_id, district_id, item['propertyPrice'], item['currencyName'], item['numberOfRoom'], item['numberOfBath'], item['propertyType'], item['propertyState'], item['buildYear'], item['squareMeter'], item['url']))
        return item

    def get_crawled_id(self) -> str:
        id = None
        try:
            sql = 'SELECT nextval(\'crawled_records_seq\')'
            self.cur.execute(sql)
            id = self.cur.fetchone()[0]
            id = self.prefix + '0'*(9-len(str(id))) + str(id)
            return id
        except Exception as e:
            print(self.cur.query)

    def get_department_id(self, departmentName) -> str:
        try:
            sql = 'SELECT department_id FROM property_department WHERE department_name like %s'
            self.cur.execute(sql, [departmentName])
            id = self.cur.fetchone()
            if (id is None):
                return 'D000'
            return id[0]
        except psycopg2.Error as e:
            print(self.cur.query)

    def get_district_id(self, departmentId, districtName) -> str:
        try:
            sql = 'SELECT pd.district_id FROM property_district pd WHERE pd.department_id = %s and pd.district_name like %s'
            self.cur.execute(sql, (departmentId, districtName))
            id = self.cur.fetchone()
            if (id is None):
                new_dist_id = self.get_new_district_id()
                sql = 'INSERT INTO property_district (department_id, district_id, district_name) VALUES (%s, %s, %s)'
                self.cur.execute(sql, ( departmentId, new_dist_id, districtName ))
                return new_dist_id
            return id[0]
        except psycopg2.Error as e:
            print(self.cur.query)

    def get_new_district_id(self) -> str:
        id = None
        try:
            sql = 'SELECT nextval(\'property_district_seq\')'
            self.cur.execute(sql)
            id = self.cur.fetchone()[0]
            id = 'S' + '0'*(3-len(str(id))) + str(id)
            return id
        except Exception as e:
            print(self.cur.query)


class InfoCasaRegions:
    conf = PgConfig()
    prefix = 'D'

    def open_spider(self, spider):
        hostname = self.conf.get_host()
        username = self.conf.get_user()
        password = self.conf.get_pass()
        database = self.conf.get_db()
        port = self.conf.get_port()
        self.conn = psycopg2.connect(host=hostname, port=port, user=username, password=password, dbname=database)
        self.cur = self.conn.cursor()
        self.conn.autocommit = True

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        if self.track_exists_dep(item['infocasaDepId']):
            return item
        sql = 'INSERT INTO property_department ( department_id, department_name, infocasa_country_id, infocasa_dep_id ) VALUES ( %s, %s, %s, %s )'
        self.cur.execute(sql, (self.get_dep_id(), item['departmentName'], int(item['infocasaCountryId']), int(item['infocasaDepId'])))
        return item

    def track_exists_dep(self, track_id):
        try:
            sql = 'SELECT * FROM property_department WHERE infocasa_dep_id = %s'
            self.cur.execute(sql, [int(track_id)])
            return (self.cur.fetchone() is not None)
        except psycopg2.Error as e:
            print(self.cur.query)

    def get_dep_id(self) -> str:
        id = None
        try:
            sql = 'SELECT nextval(\'property_department_seq\')'
            self.cur.execute(sql)
            id = self.cur.fetchone()[0]
            id = self.prefix + '0'*(3-len(str(id))) + str(id)
            return id
        except Exception as e:
            print(self.cur.query)