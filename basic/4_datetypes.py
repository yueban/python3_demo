# coding=utf-8

# Number

# n = 0x20
# print(n)
# n = 0o20
# print(n)


# a = 1.0
# print(a)
# a = int(a)
# print(a)
# a = float(a)
# print(a)
# print(complex(a))
# print(complex(a, a))


# # calculate fucntion
# import math

# print( '%-25s%s'  %('abs(-10)',abs(-10)))
# print( '%-25s%s'  %('round(4.1)',round(4.1)))
# print( '%-25s%s'  %('max(2, 1)',max(2, 1)))
# print( '%-25s%s'  %('min(2, 1)',min(2, 1)))
# print( '%-25s%s'  %('math.ceil(4.1)',math.ceil(4.1)))
# print( '%-25s%s'  %('math.floor(4.1)',math.floor(4.1)))
# print( '%-25s%s'  %('math.fabs(-10)',math.fabs(-10)))
# print( '%-25s%s'  %('math.log(100, 10)',math.log(100, 10)))
# print( '%-25s%s'  %('math.pow(2, 3)',math.pow(2, 3)))
# print( '%-25s%s'  %('math.sqrt(9)',math.sqrt(9)))
# print( '%-25s%s'  %('math.modf(4.1)',math.modf(4.1)))


# # random fucntion
# import random

# print('%-40s%s' % ('random.choice(range(10)):', random.choice(range(10))))
# print('%-40s%s' % ('random.randrange(1, 20, 2):', random.randrange(1, 20, 2)))
# print('%-40s%s' % ('random.random():', random.random()))
# l = [1, 2, 3, 4, 5]
# random.shuffle(l)
# print('%-40s%s' % ('random.shuffle([1, 2, 3, 4, 5]):', l))
# print('%-40s%s' % ('random.uniform(1, 3):', random.uniform(1, 3)))


# # trigonometric fucntion
# import math

# print('%-30s%s' % ('math.sin(math.pi / 6):', math.sin(math.pi / 6)))
# print('%-30s%s' % ('math.cos(math.pi / 6):', math.cos(math.pi / 6)))
# print('%-30s%s' % ('math.tan(math.pi / 4):', math.tan(math.pi / 4)))
# print('%-30s%s' % ('math.degrees(math.pi / 2):', math.degrees(math.pi / 2)))
# print('%-30s%s' % ('math.radians(180):', math.radians(180)))


# # math const
# import math

# print('%-35s%s' % ('math.pi:',   math.pi))
# print('%-35s%s' % ('math.e:',   math.e))
# print('%-35s%s' % ('math.pi == math.radians(180):',   math.pi == math.radians(180)))



# String, List, Tuple, Dictionary
# 相关函数使用时查询文档



# Set
s = {'ranran', 'alice', 'emma'}
print(s)
s.add(3)
s.add((1, 2, 3))
# s.add(['a', 'c'])
s.update(['a', 'c'])
print(s)
s.remove(3)
print(s)
# s.remove(3)
s.discard(3)
print(len(s))
print(3 not in s)
s.clear()
