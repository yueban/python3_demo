# coding=utf-8


# def plus(a, b):
#     return a+b

# print(plus(1, 2))


# def changeInt(a):
#     a = 10

# b = 1
# changeInt(b)
# print(b)


# def changeList(l):
#     l[0] = 10

# l = [1, 2, 3]
# changeList(l)
# print(l)


# def printInfo(name, age=10, *vartuple):
#     print('name: %s\tage: %d' % (name, age))
#     for x in vartuple:
#         print(x)

# printInfo('ranran')
# printInfo(age=5, name='ranran')
# printInfo('ranran', 1, 1, 2, 3)


# def printInfo(name, age=10, **vardict):
#     print('name: %s\tage: %d' % (name, age))
#     print(vardict)

# printInfo('ranran', 5, alice=3, emma=4)


# def plus(a, b, *, c):
#     print(a+b+c)

# # plus(1, 2, 3)
# plus(1, 2, c=3)


# sum = lambda a, b : a + b
# print(sum(1, 2))


# # scope: L –> E –> G –>B
# # L （Local） 局部作用域
# # E （Enclosing） 闭包函数外的函数中
# # G （Global） 全局作用域
# # B （Built-in） 内建作用域

# x = int(2.9)  # 内建作用域: int, 全局作用域: x

# g_count = 0  # 全局作用域: g_count
# def outer():
#     o_count = 1  # 闭包函数外的函数中: o_count
#     def inner():
#         i_count = 2  # 局部作用域: i_count

# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域

# if True:
#     a = 1
# print(a)

# while True:
#     n = 10
#     break
# print(n)

# def f():
#     a = 10

# print(a)


# # keyword: global
# num = 1

# def f():
#     # wrong
#     # print(num)
#     # num = 123

#     # correct
#     global num
#     print(num)
#     num = 123

# f()
# print(num)


# a = 10

# def test():
#     # wrong
#     # a = a+1

#     # correct
#     global a
#     a = a+1

#     print(a)

# test()


# # keyword: nonlocal
# def outer():
#     num = 10

#     def inner():
#         # num not changed
#         # num = 5
#         # print(num)

#         # num changed
#         nonlocal num
#         num = 5
#         print(num)

#     inner()
#     print(num)

# outer()
