# coding=utf-8

"""
模拟豆瓣登录
"""

import time
import requests
import getpass
from bs4 import BeautifulSoup


class DoubanCrawl:
    __login_url = 'https://www.douban.com/'
    __login_post_url = 'https://www.douban.com/accounts/login'
    __personal_url = 'https://www.douban.com/mine/'
    # __personal_url = 'https://www.douban.com/people/60229359/'
    __setting_url = 'https://www.douban.com/settings/'
    __captcha_img_url_template = 'https://www.douban.com/misc/captcha?id={}&size=s'

    def __init__(self, username, password):
        self. headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Referer': 'https://www.douban.com/',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
        }

        self.session = requests.session()
        self.username = username
        self.password = password

    def getLoginInfo(self):
        data = {
            'source': 'index_nav',
            'form_email': self.username,
            'form_password': self.password,
        }

        html = self.session.get(self.__login_url, headers=self.headers).content
        soup = BeautifulSoup(html, 'lxml')

        captcha_div = soup.select('div[class="captcha_block"]')
        if len(captcha_div) != 0:
            captcha_id = soup.select(
                'input[name="captcha-id"]')[0].get('value')

            data['captcha-id'] = captcha_id
            data['captcha-solution'] = self.getCaptchaCode(captcha_id)

        return data

    def getCaptchaCode(self, captcha_id):
        captcha_img_url = self.__captcha_img_url_template.format(captcha_id)
        # print(captcha_img_url)
        captcha_img = self.session.get(captcha_img_url, headers=self.headers)
        with open('spider/captcha_code.jpg', 'wb') as f:
            f.write(captcha_img.content)
        return input('enter captcha code: ')

    def login(self):
        data = self.getLoginInfo()
        self.session.post(self.__login_post_url,
                          data=data, headers=self.headers)

    def getPersonalInfo(self):
        html = self.session.get(self.__personal_url, headers=self.headers)
        return html.text

    def printFollowList(self):
        html = self.session.get(self.__personal_url, headers=self.headers)
        soup = BeautifulSoup(html.content, 'lxml')
        friend_div = soup.select('div[id="friend"]')[0]
        soup_friends = BeautifulSoup(str(friend_div), 'lxml')
        a_friends = soup_friends.select('dd > a')

        friends = []
        for a_friend in a_friends:
            friend = {}
            friend['name'] = a_friend.string
            friend['href'] = a_friend.get('href')
            friends.append(friend)

        print(friends)

    def getSettingInfo(self):
        html = self.session.get(self.__setting_url, headers=self.headers)
        return html.text


if __name__ == '__main__':
    username = input('enter username: ')
    password = getpass.getpass('enter password: ')
    douban = DoubanCrawl(username, password)
    douban.login()

    douban.printFollowList()

    # with open('spider/personl_info.html', 'w') as f:
    #     f.write(douban.getPersonalInfo())

    # with open('spider/setting_info.html', 'w') as f:
    #     f.write(douban.getSettingInfo())
