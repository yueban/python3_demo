# coding=utf-8

# l = [1, 2, 3, 4]
# it = iter(l)
# print(next(it))
# print(next(it))
# print(next(it))


# l = [1, 2, 3, 4]
# it = iter(l)
# for x in it:
#     print(x)


# import sys
# l = [1, 2, 3, 4]
# it = iter(l)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


# import sys

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 10:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration

# n = MyNumbers()
# it = iter(n)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


import sys

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter >= n:
            return
        yield b
        a, b = b, a+b
        counter += 1

f = fibonacci(10)
while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()
