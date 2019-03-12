# coding=utf-8

import os
import re
import queue
import random
import requests
import json

from time import sleep
from threading import Thread
from bs4 import BeautifulSoup


class ComicSpider(object):
    """
    section = {
        name,
        url,
        size,
        pages: [page1, page2]
        parseQueue: queue
        downloadQueue: queue
        parseCounter: int
        downloadCounter: int
    }
    page = {
        index,
        url,
        imgUrl
    }    
    """

    def __init__(self, url):
        self.url = url

        self.sections = []

    def getAllSections(self):
        print('start get sectoins from : %s' % self.url)
        html = requests.get(self.url, timeout=10)
        soup = BeautifulSoup(html.content, 'lxml')
        ul_tag = soup.find_all('ul',  {'id': 'g1'})
        soup1 = BeautifulSoup(str(ul_tag[0]), 'lxml')

        for li_tag in soup1.find_all('li'):
            soup2 = BeautifulSoup(str(li_tag), 'lxml')
            a_tag = soup2.find_all('a')
            href_list = re.findall(re.compile('href="(.+?)"'), str(a_tag))
            titleList = re.findall(re.compile('title="(.+?)"'), str(a_tag))
            if len(href_list) != 0 and len(titleList) != 0:
                section = {}
                section['name'] = titleList[0]
                section['url'] = href_list[0]
                self.sections.append(section)

        return self.sections

    def crawlSection(self, sectionIndex):
        section = self.sections[sectionIndex]
        name = section['name']
        url = section['url']
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'lxml')
        select_tag = soup.find_all('select', {'id': 'p__select'})
        soup1 = BeautifulSoup(str(select_tag[0]), 'lxml')

        # init section data
        section['pages'] = []
        section['parseQueue'] = queue.Queue()
        section['downloadQueue'] = queue.Queue()
        section['parseCounter'] = 0
        section['downloadCounter'] = 0
        # get all pages
        all_option_tags = soup1.find_all('option')
        section['size'] = len(all_option_tags)
        for index, option_tag in enumerate(all_option_tags):
            url = option_tag.get_attribute_list('value')[0]

            page = {}
            page['num'] = index + 1
            page['url'] = url

            section['pages'].append(page)
            section['parseQueue'].put(page)

        # start parse threads
        threads_parse = []
        for i in range(0, 10):
            t = Thread(target=self.parseImgUrl, args={
                sectionIndex}, name='Thread-parseImgUrl')
            threads_parse.append(t)
        for i in range(len(threads_parse)):
            threads_parse[i].start()

        # start download threads
        threads_download = []
        for i in range(0, 10):
            t = Thread(target=self.downloadImg, args={
                sectionIndex}, name='Thread-downloadImg')
            threads_download.append(t)
        for i in range(len(threads_download)):
            threads_download[i].start()

        # join threads
        for i in range(len(threads_parse)):
            threads_parse[i].join()
        for i in range(len(threads_download)):
            threads_download[i].join()

    def parseImgUrl(self, sectionIndex):
        section = self.sections[sectionIndex]
        while not section['parseCounter'] == section['size']:
            page = section['parseQueue'].get()
            section['parseCounter'] += 1

            html = requests.get(page['url'])
            if html.status_code == 200:
                soup = BeautifulSoup(html.content, 'lxml')
                div_tag = soup.find_all('div', id='pictureContent')
                soup1 = BeautifulSoup(str(div_tag[0]), 'lxml')

                for img_tag in soup1.find_all('img', src=re.compile('.+?')):
                    soup2 = BeautifulSoup(str(img_tag), 'lxml')
                    if soup2.img['src'] is not None:
                        imgUrl = soup2.img['src']
                        page['imgUrl'] = imgUrl
                        print('<fetched> (s%s - p%s): %s' %
                              (sectionIndex, page['num'], imgUrl))
                        section['downloadQueue'].put(page)

                sleep(random.randint(2, 3))
            else:
                pass

    def downloadImg(self, sectionIndex):
        section = self.sections[sectionIndex]
        while not section['downloadCounter'] == section['size']:
            page = section['downloadQueue'].get()
            section['downloadCounter'] += 1
            html = requests.get(page['imgUrl'])

            # create folder
            imgDirPath = 'spider/imgs'
            if not os.path.exists(imgDirPath):
                os.makedirs(imgDirPath)

            # download imgFile
            picture_path = '%s/pic%s.jpg' % (imgDirPath, page['num'])
            with open(picture_path, 'wb') as f:
                f.write(html.content)

            print('<downloaded> (s%s - p%s): %s' %
                  (sectionIndex, page['num'], page['imgUrl']))

            sleep(random.randint(2, 3))


if __name__ == '__main__':
    spider = ComicSpider('http://www.hanhande.com/manhua/yiquanchaoren/')
    sections = spider.getAllSections()
    # print(json.dumps(sections, sort_keys=True, indent=2, ensure_ascii=False))
    spider.crawlSection(4)

    # print(json.dumps(sections[4], sort_keys=True,
    #                  indent=2, ensure_ascii=False))
