# coding=utf-8

# while True:
#     try:
#         s = input('Enter a number: ')
#         num = int(s)
#         print('number is %d' % num)
#     except ValueError:
#     # except (ValueError, RuntimeError):
#         print('\'%s\' is not a number' % s)


# import sys
# try:
#     f = open('f_test.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print('OS error: {0}'.format(err))
# except IOError:
#     print('cannot open file')
# except ValueError:
#     print('could not convert data to an integer')
# except:
#     print('Unexcepted error:', sys.exc_info()[0])
#     # throw the error
#     raise
# else:
#     print('convert success, number is %d' % i)
#     f.close()


# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return repr(self.value)

# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('My exception occurred:', e.value)

# raise MyError('oops!')


try:
    raise KeyboardInterrupt
finally:
    print('bye!')
