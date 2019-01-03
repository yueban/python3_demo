# coding=utf-8

# list function
# 使用时查询文档


# l = [2, 3, 4]
# print([x*3 for x in l])
# print([[x, x*3] for x in l])
# print([x*2 for x in l if x % 2 == 0])

# l = ['  a', ' b ', 'c']
# print([x.strip() for x in l])

# l1 = [2, 3, 4]
# l2 = [-4, -5, -6]
# print([x*y for x in l1 for y in l2])
# print([l1[i] * l2[i] for i in range(len(l1))])

# import math
# print([round(math.pi, i) for i in range(1, 6)])


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]

# print([
#     [row[i] for row in matrix] for i in range(len(matrix[0]))
# ])

# transposed = []
# for i in range(len(matrix[0])):
#     transposed.append([row[i] for row in matrix])
# print(transposed)

# transposed = []
# for i in range(len(matrix[0])):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)


# t = 1, 2, 3
# print(t)
# t = t, (4, 5)
# print(t)
# t = t, (6, (7, 8))
# print(t)


# a = {x for x in 'abcdabc' if x not in 'ab'}
# print(a)


# a = {x: x ** 2 for x in (2, 3, 4)}
# print(a)

# for k, v in a.items():
#     print(k, v)


# l = ['alice', 'ranran', 'emma']
# for i, v in enumerate(l):
#     print(i, v)

# names = ['alice', 'ranran', 'emma']
# ages = [4, 5, 3]
# for name, age in zip(names, ages):
#     print(name, age)

# l = [1, 2, 3, 4]
# for i in reversed(l):
#     print(i)

l = [2, 4, 3, 1]
for i in sorted(l):
    print(i)
