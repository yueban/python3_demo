# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re


def list2str(value):
    new = ''.join(value).strip()
    return new


class AnjukePipeline(object):
    def process_item(self, item, spider):
        price = item['price']
        mode = item['mode']
        area = item['area']
        floor = item['floor']
        age = item['age']
        location = item['location']
        district = item['district']

        modes = list2str(mode)

        item['price'] = int(re.findall(r'\d+', list2str(price))[0])
        item['mode'] = modes.replace('\t', '').replace('\n', '')
        item['area'] = int(re.findall(r'\d+', list2str(area))[0])
        item['floor'] = list2str(floor)
        item['age'] = int(re.findall(r'\d+', list2str(age))[0])
        item['location'] = list2str(location)
        item['district'] = list2str(district)

        return item
