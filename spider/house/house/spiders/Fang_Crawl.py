# coding=utf-8

import scrapy
import re
import time
import pymongo
from pyquery import PyQuery as pq


class FangCrawl(scrapy.Spider):
    name = 'fangtianxia'
    __host = 'http://esf.fang.com'
    __base_url = 'http://esf.fang.com/house/i3{}/'
    start_urls = [__base_url.format(1)]

    def __init__(self):
        scrapy.Spider.__init__(self)
        db_client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = db_client['house']
        self.col = db[self.name]

    def parse(self, response):
        doc = pq(response.text)
        cur_page = int(doc('div.page_al span.on').text())
        page_count_tag_content = pq(doc('div.page_al').children()[-1]).text()
        page_count = int(re.compile(
            r'\D*(\d+)\D*').match(page_count_tag_content).group(1))

        # self.log('cur_page:{}, page_count:{}'.format(cur_page, page_count))

        if cur_page < page_count:
            url_next_page = self.__base_url.format(cur_page + 1)
            yield scrapy.Request(url_next_page, callback=self.parse)

        house_links = doc('dt.floatl > a')
        for house_link in house_links:
            url = '{}{}'.format(self.__host, pq(house_link).attr('href'))
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        doc = pq(response.text)

        price = doc('div.trl-item.price_esf.sty1 > i').text()

        refer_payment = ''
        refer_payment_tag_children = doc('div.rel.floatl').children()
        if refer_payment_tag_children:
            refer_payment_tag_content = pq(
                refer_payment_tag_children[0]).text()
            m = re.compile(
                r'\D*(\d+\.?\d*)\D*').match(refer_payment_tag_content)
            if m:
                refer_payment = m .group(1)

        # 月供是根据带宽方案不同动态计算的，这里直接获取没有数据
        monthly_payment = doc('i#FirstYG').text()

        tt_tags = doc('div.tt')
        structure = pq(tt_tags[0]).text()

        area = ''
        m = re.compile(r'\D*(\d+)\D*').match(pq(tt_tags[1]).text())
        if m:
            area = m .group(1)

        unit_price = ''
        m = re.compile(r'\D*(\d+)\D*').match(pq(tt_tags[2]).text())
        if m:
            unit_price = m.group(1)

        floor = pq(tt_tags[4]).text()
        toword = pq(tt_tags[3]).text()
        other_info = pq(tt_tags[5]).text()

        building_date = ''
        building_type = ''
        publish_date = ''
        other_tags = doc('div.cont.clearfix > div.text-item.clearfix')
        for tag in other_tags:
            pq_tag = pq(tag)
            content = pq_tag.text()
            if '建筑年代' in content:
                m = re.compile(
                    r'\D*(\d+)\D*').match(pq_tag('span.rcont').text())
                if m:
                    building_date = m.group(1)
            elif '建筑类别' in content:
                building_type = pq_tag('span.rcont').text()
            elif '挂牌时间' in content:
                publish_date = pq_tag('span.rcont').text()

        location_city = doc('div.s2 > div.s4Box > a').text()
        location_community = doc('a#kesfsfbxq_A01_01_05').text()
        locaiton_area = doc('a#kesfsfbxq_C03_08').text()
        location_district = doc('a#kesfsfbxq_C03_07').text()
        community_average_price = doc(
            'div.topt.clearfix>div>span.rcont>i').text()
        community_onsale_info = doc('a#kesfsfbxq_A01_04_01').text()
        community_rent_info = doc('a#kesfsfbxq_A01_04_03').text()
        community_info = '{} {} {}'.format(
            community_average_price, community_onsale_info, community_rent_info)
        web_url = str(response.request.url)
        web_title = doc('title').text()
        update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        _id = web_url[web_url.rindex('/') + 1:].split('.')[0]

        house = {
            '_id': _id,
            'price': price,
            'refer_payment': refer_payment,
            'monthly_payment': monthly_payment,
            'structure': structure,
            'area': area,
            'unit_price': unit_price,
            'floor': floor,
            'toword': toword,
            'other_info': other_info,
            'building_date': building_date,
            'building_type': building_type,
            'publish_date': publish_date,
            'location_city': location_city,
            'location_community': location_community,
            'locaiton_area': locaiton_area,
            'location_district': location_district,
            'community_info': community_info,
            'web_url': web_url,
            'web_title': web_title,
            'update_time': update_time,
        }
        self.col.update({'_id': house['_id']}, house, upsert=True)
