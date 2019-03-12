# coding=utf-8

import urllib.request
import urllib.error
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

headers = {
    'Accept-Encoding': 'deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

movieCategory = ['热门', '最新', '经典', '可播放', '豆瓣高分', '冷门佳片', '华语',
                 '欧美', '韩国', '日本', '动作 喜剧', '爱情', '科幻', '悬疑', '恐怖', '文艺']

movieInfoHot = []
movieInfoTime = []
movieInfoComment = []
commandCache = []
movieDetailInfo = []


class DoubanMovieSpider(object):
    """
    get movie info from douban.com
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.douban_url_base = 'https://movie.douban.com/'
        self.url_category = ''
        self.url_picture = ''
        self.url_movieDetailInfo = []

    def cvt_cmd_to_ctgy_url(self, command):
        """
        url_category: https://movie.douban.com/explore
        could also be extended to others like reading books, music, etc.
        :param command:
        :return:
        """
        if '电影' in command:
            self.url_category = self.douban_url_base + 'explore'

    def browser_hotopen(self):
        """
        hotopen chrome before sender type in any words
        :return:
        """
        self.driver.get(self.douban_url_base)

    def browser_action_general_info(self, type_command):
        self.driver.get(self.url_category)
        sleep(1)
        for num in range(0, len(movieCategory)):
            if type_command == movieCategory[num]:
                self.driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[1]/div/div[2]/div[1]'
                    '/form/div[1]/div[1]/label[{}]'.format(num+1)).click()
        sleep(1)
        self.browser_crawl_general_info()
        return movieInfoHot + movieInfoTime + movieInfoComment

    def browser_crawl_general_info(self):
        del movieInfoHot[:]
        del movieInfoTime[:]
        del movieInfoComment[:]
        for num in range(1, 4):
            self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/div[2]/div'
                '[1]/form/div[3]/div[1]/label[{}]/input'.format(num)).click()

            sleep(1)
            for counter in range(1, 11):
                if num == 1:
                    movieInfoHot.append(self.get_movie_general_info(counter))
                elif num == 2:
                    movieInfoTime.append(self.get_movie_general_info(counter))
                elif num == 3:
                    movieInfoComment.append(
                        self.get_movie_general_info(counter))
                else:
                    pass
        self.clean_general_info()

    def get_movie_general_info(self, counter):
        each_movie_info = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]'
            '/div/div[4]/div/a[{}]/p'.format(counter)).text
        return each_movie_info

    @staticmethod
    def clean_general_info():
        for num in range(0, len(movieInfoHot)):
            movieInfoHot[num] = movieInfoHot[num].replace(' ', ':  ')
            movieInfoTime[num] = movieInfoTime[num].replace(' ', ':  ')
            movieInfoComment[num] = movieInfoComment[num].replace(' ', ':  ')
            movieInfoHot[num] = str(num+1) + '.' + movieInfoHot[num] + '分'
            movieInfoTime[num] = str(num+1) + '.' + movieInfoTime[num] + '分'
            movieInfoComment[num] = str(
                num+1) + '.' + movieInfoComment[num] + '分'

    def browser_action_detail_info(self, counter, movie_name):
        movie_click_num = 0
        for num in range(0, len(movieCategory)):
            if commandCache[0] == movieCategory[num]:
                self.driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[1]/div/div[2]/div[1]'
                    '/form/div[1]/div[1]/label[{}]'.format(num+1)).click()
        sleep(1)
        # click the sequence type
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div[2]/div'
            '[1]/form/div[3]/div[1]/label[{}]/input'.format(counter)).click()
        sleep(1)
        if counter == 1:
            for i in range(0, len(movieInfoHot)):
                if movie_name in movieInfoHot[i]:
                    movie_click_num = i+1
        elif counter == 2:
            for i in range(0, len(movieInfoTime)):
                if movie_name in movieInfoTime[i]:
                    movie_click_num = i+1
        else:
            for i in range(0, len(movieInfoComment)):
                if movie_name in movieInfoComment[i]:
                    movie_click_num = i+1
        movie_detail_url = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div[4]/div/a[{}]'
            .format(movie_click_num)).get_attribute('href')
        return movie_detail_url

    @staticmethod
    def download_detail_info_html(url_target):
        try:
            req = urllib.request.Request(url_target, headers=headers)
            res = urllib.request.urlopen(req)
            result = res.read().decode('utf-8')
            return result
        except urllib.error.HTTPError as e:
            if hasattr(e, 'code'):
                print('err code: %s' % e.code)
        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                print('err reason: %s' % e.reason)

    @staticmethod
    def parse_detail_info(html_result):
        del movieDetailInfo[:]

        movie_name = ''
        actor_name_list = '主演: '
        director_name = '导演: '
        movie_type = '类型: '
        movie_date = '上映日期: '
        movie_runtime = '片长: '
        soup = BeautifulSoup(html_result, 'lxml')

        movie_name = movie_name + soup.find('span', property='v:itemreviewed').string.strip()\
            + soup.find('span', class_='year').string.strip()
        director_name = director_name + \
            soup.find('a', rel='v:directedBy').string.strip()
        for x in soup.find_all('a', rel='v:starring'):
            actor_name_list = actor_name_list + x.string.strip() + '/'
        for x in soup.find_all('span', property='v:genre'):
            movie_type = movie_type + x.string.strip() + '/'
        for x in soup.find_all('span', property='v:initialReleaseDate'):
            movie_date = movie_date + x.string.strip() + '/'
            movie_runtime = movie_runtime + \
                soup.find('span', property='v:runtime').string.strip()

        movieDetailInfo.append(movie_name)
        movieDetailInfo.append(director_name)
        movieDetailInfo.append(actor_name_list)
        movieDetailInfo.append(movie_type)
        movieDetailInfo.append(movie_date)
        movieDetailInfo.append(movie_runtime)


if __name__ == '__main__':
    spider = DoubanMovieSpider()
    # spider.url_category = 'https://movie.douban.com/explore'
    command = '电影'
    spider.browser_hotopen()
    spider.cvt_cmd_to_ctgy_url(command)
    # get movie info by type
    print('----请选择一种类型----')
    for i in range(len(movieCategory)):
        print('%d:%s' % (i+1, movieCategory[i]))

    category = ''
    while True:
        categoryInput = input('请输入类型序号或名称:')
        try:
            categoryIndex = int(categoryInput) - 1
            category = movieCategory[categoryIndex]
        except (ValueError, IndexError):
            category = categoryInput
            pass
        if category in movieCategory:
            break
        else:
            print('输入有误')

    print()
    print('正在查找' + category + '电影...')
    del commandCache[:]
    commandCache.append(category)
    movie_info_all = spider.browser_action_general_info(category)
    print('\n----按热度排序----\n' + '\n'.join(movieInfoHot))
    print('\n----按时间排序----\n' + '\n'.join(movieInfoTime))
    print('\n----按评论排序----\n' + '\n'.join(movieInfoComment))

    # get movie detail info
    search_num = -1
    totalCount = len(movie_info_all)
    while search_num == -1:
        titleInput = input('请选择要查看的影片详情:')
        for i in range(0, totalCount):
            if titleInput in movie_info_all[i]:
                if 0 <= i < 10:
                    search_num = 1
                elif 10 <= i < 20:
                    search_num = 2
                else:
                    search_num = 3
                break
            elif i == totalCount - 1:
                print('输入有误')

    url_result = spider.browser_action_detail_info(search_num, titleInput)
    html_result = spider.download_detail_info_html(url_result)
    spider.parse_detail_info(html_result)
    print(movieDetailInfo)
