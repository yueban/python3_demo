# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    """
    publish_date: 挂牌时间 (2016/11/6)
    price: 售价(万元) (260.00)
    unit_price: 单价(元) (109,290.00)
    refer_payment: 参考首付（万元） (120.00)
    monthly_payment: 月供(元) (19,290.00)
    structure: 房屋构成 (1室0厅)
    floor: 楼层 (中楼层(共7层))
    toword: 朝向 (北)
    other_info: 其它信息 (平层)
    area: 房屋大小 (24)
    building_date: 建造年份 (2003)
    building_type: 建筑楼型 (塔楼)
    location_city: 所在城市 (北京)
    location_community: 所在小区名 (兴隆都市馨园)
    locaiton_area: 所在地区 (兴隆都市馨园-东城崇文门)
    location_district: 所在城区 (东城)
    community_info: 该小区其它情况 (目前有 15套房源 出售中，挂牌均价99963元/平)
    web_url: 网页网址 (http://bj.lianjia.com/chengjiao/101100685511.html)
    web_title: 网页标题 (兴隆都市馨园 1室0厅 24平米_崇文门兴隆都市馨园二手房价格(北京链家网))
    update_time: 采集时间 (2016/11/21 10:41)
    """
