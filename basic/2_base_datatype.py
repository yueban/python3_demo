# coding=utf-8

# counter = 100
# miles = 101.0
# name = 'yueban'

# print(type(counter))
# print(type(miles))
# print(type(name))


# a = b = c = 1
# print(a, b, c)


# a, b, c = 1, 2.0, 'yueban'
# print(a, b, c)


# datatype
# variable: Number, String, Tuple
# not variable: List, Dictionary, Set

# # Number : int, float, bool, complex
# a, b, c, d = 1, 2.0, True, 4+3j
# print(a, b, c, d)
# print(isinstance(a, int))
# print(isinstance(b, float))
# print(isinstance(c, bool))
# print(isinstance(d, complex))
# # compute
# print(3+2)
# print(3-2)
# print(3*2)
# print(3/2)
# print(3//2)
# print(3 % 2)
# print(3 ** 2)

# # String
# str = 'yueban'
# print(str)
# print(str[2])
# print(str[2:])
# print(str[1:3])
# print(str[0:-1])
# print(str * 2)
# print(str + ', hi!')

# str = 'yue\nban'
# print(str)
# str = r'yue\nban'
# print(str)

# str = 'yueban'
# str[0] = 'a'


# # del val
# a = 1
# print(a)
# del a
# print(a)


# # List
# # read list
# list = ['tom', 2, 'jerry', 3.5, True, 5+2j]
# list2 = ['jack', 3]
# print(list)
# print(list[1])
# print(list[1:])
# print(list[1:3])
# print(list * 2)
# print(list + list2)

# # write list
# a = [1, 2, 3, 4, 5]
# print(a)
# a[0] = 'str2'
# print(a)
# a[2:] = []
# print(a)


# # Tuple
# # read tuple
# tuple = ('tom', 2, 'jerry', 3.5, True, 5+2j)
# tuple2 = ('jack', 3)
# print(tuple)
# print(tuple[1])
# print(tuple[1:3])
# print(tuple[1:])
# print(tuple * 2)
# print(tuple + tuple2)

# # write tuple
# tuple[0] = 1

# # special tuple
# emptyTuple = ()
# singleElemTuple = (2,)
# print(emptyTuple)
# print(singleElemTuple)
# print(singleElemTuple == 2)

# singleElemTupleWrongWay = (2)
# print(singleElemTupleWrongWay == 2)


# # Set
# names = {'tom', 'jerry', 'jack', 'tom', 'alice', 'emma'}  # two 'tom'
# print(names)
# if 'emma' in names:
#     print('emma is in Set.')
# else:
#     print('emma is not in Set.')

# # Set compute & constructor
# setA = set('abracadabra')
# setB = set('alacazam')
# print(setA)
# print(setA - setB)
# print(setA | setB)
# print(setA & setB)
# print(setA ^ setB)


# # Dictionary
# babyDict = {}
# babyDict['baby1'] = 'ranran'
# babyDict['baby2'] = 'alice'
# babyDict['baby3'] = 'emma'
# print(babyDict)
# print(babyDict['baby2'])
# # print(dict['baby4'])
# print(babyDict.keys())
# print(babyDict.values())

# # constructor
# babyDict2 = dict(
#     [{'wybaby', 'ranran'}, {'lnbaby1', 'alice'}, {'lnbaby2', 'emma'}])
# print(babyDict2)

# numDict = {x: x**2 for x in(2, 4, 6)}
# print(numDict)

# babyDict3 = dict(babywy='ranran', babyln1='alice', babyln3='emma')
# print(babyDict3)


# datatype convert
print(int('2'))
print(type(int('2')))
print(tuple([1, 2, 3]))
print(type(tuple([1, 2, 3])))
# ...many other methods
