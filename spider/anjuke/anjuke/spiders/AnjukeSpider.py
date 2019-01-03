# coding=utf-8


import scrapy
from scrapy.loader import ItemLoader
from anjuke.items import AnjukeItem


class AnjukeCrawl(scrapy.Spider):
    name = 'anjuke'
    start_urls = ['https://zhengzhou.anjuke.com/sale/']

    def parse(self, response):
        # deal with authcode
        pass

        # next page link
        next_url = response.xpath('/html[1]/body[1]/div[1]/div[2]/div[4]/div[7]/a[7]/@href').extract()[0]
        print('------{}------'.format(next_url))
        if next_url:
            yield scrapy.Request(url=next_url, callback=self.parse)

        num = len(response.xpath('//*[@id="houselist-mod-new"]/li').extract())
        for i in range(1, num+1):
            url = response.xpath(
                '//*[@id="houselist-mod-new"]/li[{}]/div[2]/div[1]/a/@href'.format(i)).extract()[0]
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        house_info = response.xpath('//*[@class="houseInfo-wrap"]')
        if house_info:
            l = ItemLoader(AnjukeItem(), house_info)
            l.add_xpath('mode', '//div/div[2]/dl[1]/dd/text()')
            l.add_xpath('area', '//div/div[2]/dl[2]/dd/text()')
            l.add_xpath('floor', '//div/div[2]/dl[4]/dd/text()')
            l.add_xpath('age', '//div/div[1]/dl[3]/dd/text()')
            l.add_xpath('price', '//div/div[3]/dl[2]/dd/text()')
            l.add_xpath('location', '//div/div[1]/dl[1]/dd/a/text()')
            l.add_xpath('district', '//div/div[1]/dl[2]/dd/p/a[1]/text()')
            yield l.load_item()
