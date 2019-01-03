# coding=utf-8


import requests
import time
import re
import json
from time import sleep


class WxCrawl():
    # {0}: timestamp
    __login_page_url = 'https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}'

    # {0}: uuid (eg. IahUfXMFOg==)
    __qrcode_url = 'https://login.weixin.qq.com/qrcode/{0}'

    # {0}: uuid (eg. IahUfXMFOg==)
    # {1}: tip (在扫码前后值不同)
    # {2}: (unknown)
    # {3}: timestamp
    __login_url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip={1}&r={2}&_={3}'

    # {0}: 通过 __login_url 扫码登录后得到
    __redirect_uri_url = '{0}&fun=new&version=v2'

    # {0}: (unknown)
    # {1}: 通过 __redirect_uri_url 得到
    __init_url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r={0}&pass_ticket={1}'

    # {0}: 通过 __redirect_uri_url 得到
    # {1}: (unknown)
    # {2}: (unknown)
    # {3}: 通过 __redirect_uri_url 得到
    __contact_url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?pass_ticket={0}&r={1}&seq={2}&skey={3}'

    def __init__(self):
        self.headers = {
            # 'Host':	'login.wx.qq.com',
            # 'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            # 'DNT': '1',
            # 'Accept': '*/*',
            'Referer': 'https://wx.qq.com/',
            # 'Accept-Encoding':	'gzip, deflate, br',
            'Accept-Language':	'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        self.session = requests.session()
        self.tip = '0'
        # r 不知道怎么来的，先随便写一个抓包来的值: 1329983750
        self.r = '1329983750'
        # 作为 __init_url post requestBody
        self.BaseRequest = {}
        # 作为 __init_url querystring 的一个参数
        self.pass_ticket = ''

    def login(self):
        # get uuid
        login_page_url = self.__login_page_url.format(int(time.time() * 1000))
        html = self.session.get(
            login_page_url, headers=self.headers, verify=False)
        match = re.compile(
            r'[\s\S]*uuid\s*=\s*"(\w+==)"[\s\S]*').match(html.text)
        uuid = match.group(1)

        # download qrcode img
        self.downloadQrcodeImg(uuid)

        # request for login status
        login_url = self.__login_url.format(
            uuid, self.tip, self.r, int(time.time() * 1000))
        while True:
            html1 = self.session.get(
                login_url, headers=self.headers, verify=False)
            code = re.compile(
                r'[\s\S]*code\s*=\s*(\d+);[\s\S]*').match(html1.text).group(1)
            print('code: ', code)
            # 408:超时 201:已扫码 200:已登录
            if code == '201':
                self.tip = '0'
            elif code == '200':
                redirect_uri = re.compile(
                    r'[\s\S]*redirect_uri\s*=\s*"(.+)"[\s\S]*').match(html1.text).group(1)
                redirect_uri_url = self.__redirect_uri_url.format(redirect_uri)

                html2 = self.session.get(
                    redirect_uri_url, headers=self.headers, verify=False)
                match = re.compile(
                    r'[\s\S]*<skey>(.+)</skey><wxsid>(.+)</wxsid><wxuin>(.+)</wxuin><pass_ticket>(.+)</pass_ticket>[\s\S]*').match(html2.text)

                self.BaseRequest = {
                    'Skey': match.group(1),
                    'Sid': match.group(2),
                    'Uin': match.group(3),
                    # 这里用抓包得到的 DeviceID
                    'DeviceID': 'e177506140053694',
                }
                self.pass_ticket = match.group(4)
                break

    def downloadQrcodeImg(self, uuid):
        url = self.__qrcode_url.format(uuid)
        html = self.session.get(url, headers=self.headers, verify=False)
        with open('spider/qrcode.jpg', 'wb') as f:
            f.write(html.content)
        self.tip = '1'

    def init(self):
        url = self.__init_url.format(self.r, self.pass_ticket)
        params = {
            'BaseRequest': self.BaseRequest,
        }
        res = self.session.post(url, data=json.dumps(params),
                                headers=self.headers, verify=False)
        data = res.content.decode('utf-8')
        with open('spider/wx_init.json', 'w') as f:
            f.write(data)

        return json.loads(data)

    def getContactData(self):
        url = self.__contact_url.format(
            self.pass_ticket, self.r, '0', self.BaseRequest['Skey'])
        res = self.session.get(url, headers=self.headers, verify=False)
        data = res.content.decode('utf-8')
        return json.loads(data)


if __name__ == '__main__':
    wx = WxCrawl()
    wx.login()
    initData = wx.init()

    print('-----最近聊天列表-----')
    contactList = initData['ContactList']
    for index, contact in enumerate(contactList):
        print('{0}. {1}'.format(index, contact['NickName']))

    contactData = wx.getContactData()
    print('-----联系人列表-----')
    for index, contact in enumerate(contactData['MemberList']):
        print('{0}. {1}'.format(index, contact['NickName']))
