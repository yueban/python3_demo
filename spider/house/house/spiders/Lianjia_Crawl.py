# coding=utf-8

import scrapy
import re
import demjson
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from house.items import HouseItem
from pyquery import PyQuery

import platform


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    start_urls = ['https://bj.lianjia.com/ershoufang/']
    __base_url = 'https://bj.lianjia.com'

    def parse(self, response):
        # next page link
        page_node = response.xpath(
            '//div[@class="page-box house-lst-page-box"]').extract()[0]
        m = re.compile(
            r'[\s\S]*page-url="(.+)"[\s\S]*"totalPage":(\d+),"curPage":(\d+)}[\s\S]*').match(str(page_node))

        if m:
            next_url = m.group(1)
            totoalPage = int(m.group(2))
            curPage = int(m.group(3))

            if curPage < totoalPage:
                next_url = next_url.replace(r'{page}', str(curPage + 1))
                next_url = self.__base_url + next_url
                print('------{}------'.format(next_url))
                yield scrapy.Request(url=next_url, callback=self.parse)

        urls = Selector(text=response.text).xpath(
            '//a[@class="noresultRecommend img "]/@href').extract()

        for url in urls:
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        m = re.compile(
            r'[\s\S]*function\(init\){\s*init\(({[\s\S]*\'\s*})\);[\s\S]*').match(response.text)

        title = response.xpath('//h1[@class="main"]/@title').extract()[0]
        url = response.request.url
        self.log('title:{} \turl:{}'.format(title, url))

        if m:
            data = demjson.decode(m.group(1))
            item = {}
            item['title'] = title
            item['ucid'] = data['ucid']
            item['houseType'] = data['houseType']
            item['isUnique'] = data['isUnique']
            item['registerTime'] = data['registerTime']
            item['area'] = data['area']
            item['totalPrice'] = data['totalPrice']
            item['price'] = data['price']
            item['houseId'] = data['houseId']
            item['resblockId'] = data['resblockId']
            item['resblockName'] = data['resblockName']
            item['isRemove'] = data['isRemove']
            item['defaultImg'] = data['defaultImg']
            item['defaultBrokerIcon'] = data['defaultBrokerIcon']
            item['resblockPosition'] = data['resblockPosition']
            item['cityId'] = data['cityId']
            item['changedate'] = data['changedate']
            item['changenum'] = data['changenum']
            item['url'] = url
            yield item
