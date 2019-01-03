# coding=utf-8

# import re
# r = re.match('1.*', '123')
# print(r)
# print(r.span())
# print(r.group())


# import re
# line = 'Cats are smarter than dogs.'
# matchObj = re.match(r'(.*) are (.*?) .*', line)
# if matchObj:
#     print('%-20s%s' % ('matchObj.group():', matchObj.group()))
#     print('%-20s%s' % ('matchObj.group(1):', matchObj.group(1)))
#     print('%-20s%s' % ('matchObj.group(2):', matchObj.group(2)))
# else:
#     print('No match.')


# import re
# line = 'yueban'
# searchObj = re.search('y', line)
# print(searchObj)
# print(searchObj.group())
# searchObj = re.search('e', line)
# print(searchObj)
# print(searchObj.group())


# import re
# phone = '13605040355'
# # num = re.sub(r'0', '', phone)
# num = re.sub(r'0', '', phone, 1)
# print(num)


# import re


# def double(matched):
#     value = matched.group('value')
#     print(value)
#     try:
#         value = int(value)
#     except ValueError:
#         pass
#     return str(value*2)


# s = 'A1B2C3'
# print(re.sub(r'(?P<value>.)', double, s))


# import re
# pattern = re.compile(r'\d+')

# # m = pattern.match('one123two456')
# # print(m)
# m = pattern.match('one123two456', 3)
# print(m)
# print(m.group())


# import re
# l = re.findall(r'\d', '123')
# print(l)
# i = re.finditer(r'\d', '123')
# for x in i:
#     print(x)
#     print(x.group())
