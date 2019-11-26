from math import sqrt

# 需要记忆或者了解的python内置包
from math import sqrt
from collections import Counter, defaultdict, deque
import numpy as np
from itertools import compress, combinations, permutations, chain, groupby, zip_longest


# 计算进制，余数，除数等代码
def number_calculate(n):
    m = n
    while m != 0:
        m, a = divmod(m, 10)
        print(m, a)


# 获取给定数字所有的除数
from math import sqrt
def get_all_divisor(n):
    if n == 1:
        return [1]
    result = set([])
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return result


def get_all_divisor(n):
    if n == 1:
        return [1]
    result = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return result


# 求素数的四种方法
from math import sqrt
from itertools import compress


# 判断是否为一个质数
def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    # Only used to test odd numbers.
    return all(n % d for d in range(3, round(n ** 0.5) + 1, 2))


# 利用byte求素数
# Returns  a list of primes < n for n > 2
def get_primes_3(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


# 计算fibonacci
def fibonacci_numbers_up_to_n(n):
    previous = 1
    current = 1
    numbers = []
    while current <= n:
        numbers.append(current)
        previous, current = current, previous + current
    return numbers


# 去掉相邻的重复代码
def remove_consecutive_duplicates(word):
    result = ''
    if word:
        result = word[0]
        for char in word[1:]:
            if result[-1] != char:
                result += char
    return result


# 列表的相关方法
# max
# min
# avg
# abs
# len
# all
# any
# zip
# round
# char
# bin
# set
# sorted
# divmod
# eval
# sum
# ascii


# 判断九宫格是否可解
# lab 20
def grid_if_valid_and_solvable_9_puzzle(grid):
    if len(grid) != 3:
        return
    grid = [tile for row in grid for tile in row]
    try:
        grid[grid.index(None)] = 0
    except ValueError:
        pass
    if sorted(grid) != list(range(9)):
        return
    if sum(1 for i in range(8) for j in range(i + 1, 9) if grid[i] and grid[j] and grid[i] > grid[j]
           ) % 2:
        return
    return grid


# 判断是否是magic square
def is_magic_square(square):
    n = len(square)
    if any(len(line) != n for line in square):
        return False
    if {number for line in square for number in line} != set(range(1, n ** 2 + 1)):
        return False
    the_sum = n * (n ** 2 + 1) // 2
    if not_good_lines(square, the_sum):
        return False
    if not_good_lines([[square[i][j] for i in range(n)] for j in range(n)], the_sum):
        return False
    if sum(square[i][i] for i in range(n)) != the_sum:
        return False
    if sum(square[i][n - 1 - i] for i in range(n)) != the_sum:
        return False
    return True


def not_good_lines(square, the_sum):
    return any(sum(line) != the_sum for line in square)


# 动态规划

def sum_of_digits(input, n):
    if not input:
        if not n:
            return 1
        return 0
    if len(input) == 1 and int(input) == n:
        return 1
    if len(input) == 1 and int(input) == n:
        return 0
    left = sum_of_digits(input[1:], n - int(input[0]))
    right = sum_of_digits(input[1:], n)
    return left + right

    # return sum_of_digits(input[1:], n) + sum_of_digits(input[1:], n - int(input[0]))


sum_of_digits('12234', 5)


# 合并字符串（难度较高）
def can_merge(string_1, string_2, string_3):
    if not string_1 and string_2 == string_3:
        return True
    if not string_2 and string_1 == string_3:
        return True
    if not string_1 or not string_2:
        return False
    if string_1[0] == string_3[0] and can_merge(string_1[1:], string_2, string_3[1:]):
        return True
    if string_2[0] == string_3[0] and can_merge(string_1, string_2[1:], string_3[1:]):
        return True
    return False


ranks = 'first', 'second', 'third'
strings = [input(f'Please input the {rank} string: ') for rank in ranks]
last = 0
if len(strings[1]) > len(strings[0]):
    last = 1
if len(strings[2]) > len(strings[last]):
    last = 2
if last == 0:
    first, second = 1, 2
elif last == 1:
    first, second = 0, 2
else:
    first, second = 0, 1
if len(strings[last]) != len(strings[first]) + len(strings[second]) or \
        not can_merge(strings[first], strings[second], strings[last]):
    print('No solution')
else:
    print(f'The {ranks[last]} string can be obtained by merging the other two.')
