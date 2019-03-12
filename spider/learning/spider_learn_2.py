# coding=utf-8

# import urllib
# import urllib.request
# import urllib.error

# url = 'https://www.douban.com/accounts/login'

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Encoding': 'deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     # Content-Length: 72
#     'Content-Type': 'application/x-www-form-urlencoded',
#     # Cookie: bid=UWkwrXK7v8I; ll="118237"; douban-fav-remind=1; push_doumail_num=0; push_noty_num=0; viewed="30143261_2081876_3427304_3817849_4430463_2985774_11608712_7067916_26359758_25717097"; ps=y; ap_v=0,6.0
#     # DNT: 1
#     # Host: www.douban.com
#     # Origin: https://www.douban.com
#     # Referer: https://www.douban.com/
#     # Upgrade-Insecure-Requests: 1
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
# }

# value = {
#     'source': 'index_nav',
#     'form_email': '343278606@qq.com',
#     'form_password': 'qwe123456'
# }

# try:
#     data = urllib.parse.urlencode(value).encode('utf-8')
#     req = urllib.request.Request(url, data, headers)
#     res = urllib.request.urlopen(req)
#     result = res.read().decode('utf-8')
#     f = open('spider/result.txt', 'w')
#     f.write(result)
#     f.close()
# except urllib.error.HTTPError as e:
#     if hasattr(e, 'code'):
#         print('err coce: %s' % e.code)
# except urllib.error.URLError as e:
#     if hasattr(e, 'reason'):
#         print('err reason: %s' % e.reason)
# else:
#     print('request success')


# set proxy & timeout
import urllib
import urllib.request
import urllib.error
import socket

url = 'https://www.douban.com/accounts/login'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Encoding': 'deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Content-Length: 72
    'Content-Type': 'application/x-www-form-urlencoded',
    # Cookie: bid=UWkwrXK7v8I; ll="118237"; douban-fav-remind=1; push_doumail_num=0; push_noty_num=0; viewed="30143261_2081876_3427304_3817849_4430463_2985774_11608712_7067916_26359758_25717097"; ps=y; ap_v=0,6.0
    # DNT: 1
    # Host: www.douban.com
    # Origin: https://www.douban.com
    # Referer: https://www.douban.com/
    # Upgrade-Insecure-Requests: 1
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

value = {
    'source': 'index_nav',
    'form_email': '343278606@qq.com',
    'form_password': 'qwe123456'
}

proxy = {'http': '61.135.217.7:80'}

timeout = 1
socket.setdefaulttimeout(timeout)

try:
    data = urllib.parse.urlencode(value).encode('utf-8')
    req = urllib.request.Request(url, data, headers)
    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)
    res = opener.open(req)
    result = res.read().decode('utf-8')
    f = open('spider/result.txt', 'w')
    f.write(result)
    f.close()
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        print('err coce: %s' % e.code)
except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('err reason: %s' % e.reason)
except socket.timeout:
    print('socket timeout')
else:
    print('request success')
