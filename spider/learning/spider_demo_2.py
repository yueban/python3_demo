# coding=utf-8

import urllib.request
import urllib.error
import json
import pymongo
from prettytable import PrettyTable

baseUrl = 'http://fe-api.zhaopin.com/c/i/sou'
pageSize = 50

headers = {
    # Connection: keep-alive
    # Accept: application/json, text/plain, */*
    # Origin: https://sou.zhaopin.com
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    # DNT: 1
    # Referer: https://sou.zhaopin.com/?pageSize=60&jl=719&kw=Android&kt=3
    # Accept-Encoding:deflate, br
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    # Cookie: sts_deviceid=1669ef045979c5-0a784b0633716-346c780e-1296000-1669ef045984cb; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.google.com%2F; dywea=95841923.673890113709390100.1540264839.1540264839.1540264839.1; dywec=95841923; dywez=95841923.1540264839.1.1.dywecsr=google.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/; urlfrom=121114584; urlfrom2=121114584; adfcid=www.google.com; adfcid2=www.google.com; adfbid=0; adfbid2=0; sts_sid=1669f82811d454-044fd89f7f84a8-346c780e-1296000-1669f82811e8cb; ZP_OLD_FLAG=false; LastCity=%E9%83%91%E5%B7%9E; LastCity%5Fid=719; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%224ae9b4c1-734e-48ae-b1e6-fcb0df7a4fbd-sou%22%2C%22funczone%22:%22smart_matching%22}}; GUID=885a57a2adf74d8dbc5dc74604857f9e; sts_evtseq=6
}

params = {
    'pageSize': pageSize,
    'start': 0,
    'cityId': '',  # cityCode
    'workExperience': '-1',
    'education': '-1',
    'companyType': '-1',
    'employmentType': '-1',
    'jobWelfareTag': '-1',
    'kw': '',  # keyword
    'kt': '3',
    # lastUrlQuery:%7B%22pageSize%22:%2260%22,%22jl%22:%22719%22,%22kw%22:%22Android%22,%22kt%22:%223%22%7D
    # _v:0.42756943
}

# input params
cityDataFile = open('spider/spider_demo_2_cities.json', 'r')
cityList = json.loads(cityDataFile.read())
cityDataFile.close()
# cityList[0]: {'en_name': 'ALL', 'code': '489', 'name': '全国', 'sublist': []}
# print(cityList[0])

keyword = ''
while True:
    keyword = input('请输入要搜索的职位信息:').strip()
    if keyword != '':
        break
    else:
        print('搜索内容不能为空，请重新输入')
params['kw'] = keyword

print('------请选择职位所在城市------')
cityCodeList = []
for city in cityList:
    code = city['code']
    name = city['name']
    cityCodeList.append(code)
    print('%s:%s' % (code, name))
cityCode = ''
while True:
    cityCode = input('请输入城市序号:')
    if cityCode in cityCodeList:
        index = cityCodeList.index(cityCode)
        print('您选择的城市是: %s' % cityList[index]['name'])
        break
    else:
        print('输入有误，请重新输入')
params['cityId'] = cityCode

# featch data
totalCount = -1
pageIndex = 1
hasMoreData = True

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
db = myclient['spider_zhilian']
colJobs = db['jobs']
# delete all data
colJobs.delete_many({})

print('fetching data start...')
while hasMoreData:
    # update pageIndex
    params['start'] = (pageIndex - 1) * pageSize

    # request data
    url = '%s?%s' % (baseUrl, urllib.parse.urlencode(params))
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))
    results = data['data']['results']

    # update totalCount
    totalCount = int(data['data']['numFound'])

    # store data
    for job in results:
        # set _id as primary key
        job['_id'] = job['number']
        colJobs.replace_one({'_id': job['_id']}, job, True)

    # print('page: %s\tlen: %s' % (pageIndex, len(results)))
    hasMoreData = totalCount != 0 and pageIndex * pageSize < totalCount
    # print('fetching data: %d/%d: %s' %
    #       ((pageIndex-1) * pageSize + len(results), totalCount, url))
    print('fetching data: %d/%d' %
          ((pageIndex-1) * pageSize + len(results), totalCount))
    pageIndex += 1


# show result in console
allJobs = colJobs.find()

table = PrettyTable([
    'job_name',
    'company_name',
    'feedback_rate',
    'salary',
    'location'])
for job in allJobs:
    feedbackRate = float(job['feedbackRation'])
    feedbackRate = '0' if feedbackRate == 0 else '{:.1f}'.format(
        feedbackRate * 100).rstrip('0'.rstrip('.')) + '%'

    table.add_row([
        job['jobName'],
        job['company']['name'],
        feedbackRate,
        job['salary'],
        job['city']['display']])

print(table)
