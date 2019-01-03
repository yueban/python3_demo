# coding=utf-8

# s = 'Hello, yueban'
# print(str(s))
# print(repr(s))

# print(str(1/3))
# print(repr(1/3))

# s = 'Hello, yueban\n'
# print(str(s))
# print(repr(s))


# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(4), repr(x*x*x).rjust(4))

# for x in range(1, 11):
#     print('{0:2d}{1:4d}{2:5d}'.format(x, x*x, x*x*x))

# for x in range(1, 11):
#     print('%2d%4d%5d' % (x, x*x, x*x*x))

# print('{1} {0!r:s}'.format('alice\n', 'emma\n'))

# import math
# print('{:.4f}'.format(math.pi))


# d = {'alice': 4, 'emma': 3, 'ranran': 5}
# print('alice: {0[alice]}, emma: {0[emma]}, ranran: {0[ranran]}'.format(d))


# s = 'number is %d' % 2
# print(s)


# f = open('f_test.txt', 'w')
# num = f.write('Python is a beautiful language.\nYes, it\'s true.')
# f.close()
# print(num)

# f = open('f_test.txt', 'r')
# s = f.read()
# f.close()
# print(s)

# f = open('f_test.txt', 'r')
# s = f.readline()
# f.close()
# print(s)

# f = open('f_test.txt', 'r')
# lines = f.readlines()
# f.close()
# for s in lines:
#     print(s, end=' ')

# with open('f_test.txt', 'r') as f:
#     print(f.read())


# # pickle: use file to storage byte data
# import pickle
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}

# l = [1, 2, 3]
# l.append(l)

# output = open('f_data.pkl', 'wb')
# pickle.dump(data1, output)
# pickle.dump(l, output, -1)
# output.close()

# pklFile = open('f_data.pkl', 'rb')
# data1 = pickle.load(pklFile)
# data2 = pickle.load((pklFile))
# pklFile.close()
# print(data1)
# print(data2)


# File funcions: 使用时再查阅文档