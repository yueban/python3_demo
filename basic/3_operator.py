# coding=utf-8

# # Arithmetic operator
# print('2+3:\t', (2 + 3))
# print('2-3:\t', (2 - 3))
# print('2*3:\t', (2 * 3))
# print('2/3:\t', (2 / 3))
# print('2%3:\t', (2 % 3))
# print('2**3:\t', (2 ** 3))
# print('2//3:\t', (2 // 3))


# # compare operator
# print('2 == 3:\t', (2 == 3))
# print('2 != 3:\t', (2 != 3))
# print('2 > 3:\t', (2 > 3))
# print('2 < 3:\t', (2 < 3))
# print('2 >= 3:\t', (2 >= 3))
# print('2 <= 2:\t', (2 <= 2))
# print('\'str\' > \'st\':\t', 'str' > 'st')
# print('\'str\' > \'str\':\t', 'str' > 'str')


# # assignment operator
# a = 2
# print(a)
# a += 2
# print(a)
# a *= 2
# print(a)
# a -= 2
# print(a)
# a /= 2
# print(a)
# a **= 2
# print(a)
# a //= 2
# print(a)


# # bit operator
# a = 60  # 0011 1100
# b = 13  # 0000 1101
# print(a & b)  # 0000 1100 = 12
# print(a | b)  # 0011 1101 = 61
# print(a ^ b)  # 0011 0001 = 49
# print(~a)  # 1100 0011 = -61 有符号二进制数的补码形式
# print(a<<1) # 0111 1000 = 120
# print(a>>1) # 0001 1110 = 30


# # logical operator
# a = 10
# b = 20
# print(a and b)  # and: if a s False, return False; else, return b
# print(a or b)  # or: if a is True, return a; else, return b
# print(not a)  # not: if a is True, return False; else, return True


# # member operator
# print(1 in [1, 2])
# print(1 not in (1, 2))


# # identity operator
# # is / is not, determine if have the same reference
# # == determine if have the same value
# a = 1
# print(1 is 1)
# print(a is 1)
# b = '1'
# print('1' is '1')
# print(b is '1')
# print(a is b)


# operator priority
# **
# ~ + -	(正负号)
# * / % //
# + -
# >> <<
# &
# ^ |
# <= < > >=
# <> == !=
# = %= /= //= -= += *= **=
# is   is not	
# in   not in	
# and or not