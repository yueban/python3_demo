# coding=utf-8

import requests
import pymongo
import xlwings
import os
from pyquery import PyQuery as pq
from shutil import copyfile

db_client = pymongo.MongoClient('mongodb://localhost:27017/')
db = db_client['test']
table = db['ruizong_medical']


def crawlData():
    for page in range(1, 31):
        print('getting page {}...'.format(page))
        url = 'http://tieba.baidu.com/f/index/forumpark?cn=%E5%81%A5%E5%BA%B7%E4%BF%9D%E5%81%A5&ci=0&pcn=%E7%94%9F%E6%B4%BB&pci=0&ct=1&st=new&pn={}'.format(
            page)
        res = requests.get(url, verify=False)
        html = res.text
        # print(html)

        doc = pq(html)
        items = doc('div.ba_content')
        for item in items:
            item_pq = pq(item)
            name = item_pq('.ba_name').text()
            memberCount = item_pq('.ba_m_num').text()
            postCount = item_pq('.ba_p_num').text()
            desc = item_pq('.ba_desc').text()
            info = {
                'name': name,
                'memberCount': memberCount,
                'postCount': postCount,
                'desc': desc
            }
            table.update_one({'_id': name}, {'$set': info}, upsert=True)


def exportExcel():
    app = xlwings.App(visible=True, add_book=False)
    workbook = app.books.add()
    sheet = workbook.sheets('Sheet1')

    infos = table.find()
    data = [['贴吧名', '描述', '成员数量', '帖子数']]
    for info in infos:
        data.append([
            info.get('name', ''),
            info.get('desc', ''),
            info.get('memberCount', ''),
            info.get('postCount', ''),
        ])
    data_range = sheet.range('A1')
    data_range.value = data

    # 保存
    # 因 mac 对 excel 程序访问文件的限制，这里先将 excel 文件保存至有权限访问的文件夹中，再将其复制到目标文件夹中
    authPath = '/Users/yueban/Library/Group Containers/UBF8T346G9.Office/MyExcelFolder/{}'.format(
        'ruizong_medical.xlsx')
    authPath = os.path.abspath(authPath)
    if os.path.exists(authPath):
        os.remove(authPath)
    workbook.save(authPath)
    app.quit()
    # 将 excel 复制到目标文件夹
    copyfile(authPath, os.path.abspath('test.xlsx'))


# crawlData()
exportExcel()
