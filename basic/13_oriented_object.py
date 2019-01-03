# coding=utf-8

# class MyClass:
#     """a simple class"""
#     i = 123

#     def f(self):
#         return 'hello, class!'


# x = MyClass()
# print(x.i)
# print(x.f())


# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def print(self):
#         print('name: %s, age: %d' % (self.name, self.age))
#         print(self)
#         print(self.__class__)


# # x = People('alice', 4)
# # x.print()


# class Student(People):
#     def __init__(self, name, age, grade):
#         People.__init__(self, name, age)
#         self.grade = grade

#     def print(self):
#         print('name: %s, age: %d, grade: %d' %
#               (self.name, self.age, self.grade))
#         print(self)
#         print(self.__class__)


# # s = Student('ranran', 5, 2)
# # s.print()


# class Printer:
#     def __init__(self, tag, name):
#         self.tag = tag
#         self.name = name

#     def print(self):
#         print('tag: %s, name: %s' % (self.tag, self.name))


# class StudentPrinter(Printer, Student):
#     def __init__(self, tag, name, age, grade):
#         Printer.__init__(self, tag, name)
#         Student.__init__(self, name, age, grade)


# sPrinter = StudentPrinter('printer_tag', 'emma', 3, 1)
# sPrinter.print()


# class MyClass:
#     __a = 'a'
#     b = 'b'

#     def __c(self):
#         print('method c called')

#     def d(self):
#         print('method d called')


# x = MyClass()
# # print(x.__a)
# print(x.b)
# # x.__c()
# x.d()


class MyVector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return MyVector(self.a + other.a, self.b+other.b)


v1 = MyVector(2, -3)
v2 = MyVector(-4, 5)
print(v1+v2)
