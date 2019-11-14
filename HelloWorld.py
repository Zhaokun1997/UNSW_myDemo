# import re
#
# x = 123
# y = 321
#
#
# # rules:当前作用域局部变量->外层作用域变量
# # ->当前模块中的全局变量->python内置变量.
# def testlocal():
#     global x
#     global y
#     print(x + y)
#     c = x + y
#     print(c)
#     print(x)
#
#
# testlocal()
# print(x)
#
# a = 123
#
#
# def outer():
#     global a
#     a = 100
#
#     a1 = 200
#
#     def inter():
#         nonlocal a1
#         a1 = 300
#
#     inter()
#     print(a1)
#     pass
#
#
# outer()
# print(a)
#
# dic = [3, 5, 7, 6, 1, 0, 2]
# d = [{"order": 3}, {"order": 1}, {"order": 2}]
#
# while True:
#     roman_number = input("input a roman number : ")
#     upper = roman_number.upper()
#     pattern_roman = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
#     match_obj = pattern_roman.match(upper)
#     if match_obj:
#         print(upper)
#         print('input is valid.')
#     else:
#         print(upper)
#         print('input is invalid.')
import math
from itertools import compress


def get_all_divisor(n):
    if n == 1:
        return [1]
    result = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return result


# return a list of primes < n for n > 2
def get_primes_3(n):
    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


print(get_primes_3(21))
