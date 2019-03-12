# coding=utf-8

import requests
import os
import hashlib
import re
import json
from bs4 import BeautifulSoup

"""
URL	https://passport.lagou.com/login/login.json

login_post_data:

isValidate	true
username	18607006059
password	77ee3fd808166660d0b9653ff7cc2bcd
request_form_verifyCode	
submit	
challenge	a56838ccb410a348c7cdd9ad862a5b74

login_response:

{
	"content": {
		"rows": []
	},
	"message": "该帐号不存在或密码（验证码）误，请重新输入",
	"state": 400,
	"submitCode": 10430145,
	"submitToken": "f540110a-43af-422e-a52e-15133dbef590"
}

{
	"content": {
		"rows": []
	},
	"message": "操作成功",
	"state": 1,
	"submitCode": 95771052,
	"submitToken": "f26a3507-ed04-4bb2-b4b4-429180fc07f2"
}
"""

"""
POST /gt_judgement?pt=0&gt=66442f2f720bfc86799932d8ad2eb6c7 HTTP/1.1
pt	0
gt	66442f2f720bfc86799932d8ad2eb6c7

response
{"result": "slide", "api_server": "api.geetest.com", "id": "66442f2f720bfc86799932d8ad2eb6c7", "product": "sensebot", "logo": true, "static_servers": "static.geetest.com,dn-staticdown.qbox.me", "challenge": "a56838ccb410a348c7cdd9ad862a5b74", "jsFile": "/static/js/slide.7.4.1.js", "status": "success", "aspect_radio": 103}
"""


class LagouCrwal():
    __login_page_url = 'https://passport.lagou.com/login/login.html'
    __login_url = 'https://passport.lagou.com/login/login.json'

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Referer': 'https://passport.lagou.com/login/login.html',
            # 'Accept-Language':	'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        self.session = requests.session()
        self.captchaImgPath = os.path.split(os.path.realpath(__file__))[
            0] + os.sep + 'captcha.jpg'

    def login(self):
        requestData = {
            'isValidate': 'true',
            'username': '18607006059',
            'password': self.encryptPwd('wvagh45'),
            'request_form_verifyCode': '',
            'submit': '',
            # 'challenge': 'a56838ccb410a348c7cdd9ad862a5b74',
        }
        loginHeaders = self.headers.copy()
        loginHeaders.update(self.getTokenCode())

        res = self.session.post(
            self.__login_url, data=requestData, headers=loginHeaders)
        data = json.loads(res.content.decode('utf-8'))

        state = data['state']

        # 1: success
        # 400: wrong account or pwd
        if state == 1:
            return data
        else:
            print(data['message'])

    def encryptPwd(self, password):
        """
        [login.html 中引用了一个 js 文件，代码如下]
        <script type="text/javascript">
            //login page
            require(['pc/page/login/main']);
        </script>

        [其中密码加密相关代码为]
        v="veenike";g.password=md5(g.password),g.password=md5(v+g.password+v)
        """
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        # veennike 这个值是在js文件找到的一个写死的值
        password = 'veenike{}veenike'.format(password)
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        return password

    def getTokenCode(self):
        res = self.session.get(self.__login_page_url, headers=self.headers)
        soup = BeautifulSoup(res.content, 'lxml', from_encoding='utf-8')
        params = soup.find_all('script')[1].getText().strip().replace('\n', '')

        m = re.compile(
            r'\W*window.X_Anti_Forge_Token\s*=\s*\'([\w-]+)\'\W*window.X_Anti_Forge_Code\s*=\s*\'(\d+)\'\W*').match(params)

        return {
            'X-Anit-Forge-Token':  m.group(1),
            'X-Anit-Forge-Code':  m.group(2),
        }


if __name__ == '__main__':
    lagou = LagouCrwal()
    result = lagou.login()
    print(result)
