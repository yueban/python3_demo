# coding=utf-8

"""
jd 更新了登录策略，这个 demo 暂时还不能模拟登录
"""

import time
import requests
import getpass
from bs4 import BeautifulSoup


class JDCrawl:
    __login_url = 'https://passport.jd.com/new/login.aspx'
    __login_post_url = 'https://passport.jd.com/uc/loginService'
    __cart_url = 'https://cart.jd.com/cart.action'
    __order_url = 'https://order.jd.com/center/list.action'
    __auth_url = 'https://passport.jd.com/uc/showAuthCode'

    def __init__(self, username, password):
        self. headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Referer': 'https://www.jd.com/',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

        self.session = requests.session()
        self.username = username
        self.password = password

    def getLoginInfo(self):
        html = self.session.get(self.__login_url, headers=self.headers).content
        soup = BeautifulSoup(html, 'lxml')

        uuid = soup.select('input[name="uuid"]')[0].get('value')
        eid = soup.select('input[name="eid"]')[0].get('value')
        # session id
        fp = soup.select('input[name="fp"]')[0].get('value')
        # token
        _t = soup.select('input[name="_t"]')[0].get('value')
        login_type = soup.select('input[name="loginType"]')[0].get('value')
        main_flag = soup.select('input[name="main_flag"]')[0].get('value')
        pub_key = soup.select('input[name="pubKey"]')[0].get('value')
        sa_token = soup.select('input[name="sa_token"]')[0].get('value')
        useSlideAuthCode = soup.select('input[name="useSlideAuthCode"]')[
            0].get('value')

        auth_page = self.session.post(self.__auth_url, data={
            'loginName': self.username,
            'nloginpwd': self.password
        }).text

        if 'true' in auth_page:
            auth_code_url = soup.select('#JD_Verification1')[0].get('src')
            auth_code = str(self.get_auth_img(auth_code_url))
        else:
            auth_code = ''

        return {
            'uuid': uuid,
            # eid fp 暂时用一个固定的（jd 页面是在登录时调用 loginGetEid 函数动态赋值的）
            'eid': 'KE65NDB7ZWYHGRG5EI7P4H3ORWO6WX2BNLRPMWISRM6N6HLUBAUHXKLEXCWRN2CAFAUKP44P4VZDUQVWIFJBWOGNHA',
            'fp': 'f0e9bec75ef4a6d573e5e323c8517008',
            '_t': _t,
            'loginType': login_type,
            # 'main_flag': main_flag,
            'loginname': self.username,
            'nloginpwd': self.password,
            'chkRememberMe': True,
            'pubKey': pub_key,
            'sa_token': sa_token,
            'useSlideAuthCode': useSlideAuthCode,
            'authcode': auth_code,
            # seqSid 不知如何获取，暂时用一个固定的
            'seqSid': '5375640812850705000',
        }

    def get_auth_img(self, url):
        auth_code_url = 'https:{}&yys={}'.format(
            url, str(int(time.time() * 1000)))
        auth_img = self.session.get(auth_code_url, headers=self.headers)
        with open('spider/auth_code.jpg', 'wb') as f:
            f.write(auth_img.content)
        return input('enter auth code: ')

    def login(self):
        data = self.getLoginInfo()
        # print(data)
        headers = {
            'Referer': self.__login_post_url,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        res = self.session.post(self.__login_post_url,
                                data=data, headers=headers)

        with open('spider/login_result.html', 'w') as f:
            f.write(res.content.decode('unicode_escape'))

    def getCartInfo(self):
        html = self.session.post(self.__cart_url, headers=self.headers)
        return html.text

    def getOrderInfo(self):
        res = self.session.post(self.__order_url, headers=self.headers)
        return res.text


if __name__ == '__main__':
    username = input('enter username: ')
    password = getpass.getpass('enter password: ')
    jd = JDCrawl(username, password)
    jd.login()

    with open('spider/order_info.html', 'w') as f:
        f.write(jd.getOrderInfo())
    # print(jd.getOrderInfo())
    # print(jd.getCartInfo())
