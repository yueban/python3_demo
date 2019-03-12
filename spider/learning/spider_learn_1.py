# coding=utf-8

# import urllib
# import urllib.request

# response = urllib.request.urlopen('http://www.baidu.com/')
# result = response.read().decode('utf-8')
# print(result)
# print('\nresponse.geturl():\n%s' % response.geturl())
# print('\nresponse.info():\n%s' % response.info())
# print('\nresponse.getcode():\n%s' % response.getcode())


# import urllib
# import urllib.request

# headers = {'User-Agent': ''}
# req = urllib.request.Request('http://www.baidu.com/', headers=headers)
# res = urllib.request.urlopen(req)
# result = res.read().decode('utf-8')
# print(result)


import urllib.request
import urllib.error

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    # url = 'http://www.google.com/'
    url = 'http://45.32.90.24:3000/posts1'
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)
    result = res.read().decode('utf-8')
    print(result)
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        print('err code: %d' % e.code)
except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('error reason: %s' % e.reason)
else:
    print('request success')
