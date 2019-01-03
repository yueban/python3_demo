# coding=utf-8

# sum = 0
# i = 1
# while i < 100:
#     sum += i
#     i += 1
# print(sum)


# while True:
#     n = int(input('请输入一个数字: '))
#     print('你输入的数字是: %d' % n)


# edge = 10
# n = int(input('请输入一个大于%d的整数: ' % edge))
# while n < 10:
#     print('输入错误,%d小于%d' % (n, edge))
#     n = int(input('请输入一个大于%d的整数: ' % edge))
# else:
#     print('输入正确,%d大于%d' % (n, edge))


# while True: print('one line while.')


# for i in range(10):
#     print(i)


# l = ['alice', 'ranran', 'emma']
# for i in range(len(l)):
#     print(i, l[i])


# for letter in 'yueban':
#     if letter == 'e':
#         continue
#     print(letter)
#     if letter == 'a':
#         break


# edge = 20
# for n in range(2, edge):
#     for x in range(2, n):
#         if n % x == 0:
#             print('%d = %d * %d' % (n, x, n//x))
#             break
#     else:
#         print('%d 是质数' % (n))


for letter in 'yueban':
    if letter == 'e':
        pass
        print('there is a pass')
    print('current letter is %s' % letter)
