# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 4


'''
Will be tested with a at equal equal to 2 and b at most equal to 10_000_000.
'''

import sys
from math import sqrt
from itertools import compress


def f(a, b):
    number_of_primes_at_most_equal_to_b = 0

    #     prime_a = get_all_prime(a)
    #     prime_b = get_all_prime(b + 1)
    #     # print(f'all primes that less than {a} are : ', prime_a)
    #     # print(f'all primes that less than {b} are : ', prime_b)
    #     number_of_primes_at_most_equal_to_b = len(prime_b) - len(prime_a)
    #     if a == 2:
    #         number_of_primes_at_most_equal_to_b += 1
    #     if not number_of_primes_at_most_equal_to_b:
    #         print(f'There is no prime number beween {a} and {b}.')
    #     elif number_of_primes_at_most_equal_to_b == 1:
    #         print(f'There is a unique prime number beween {a} and {b}.')
    #     else:
    #         print(f'There are {number_of_primes_at_most_equal_to_b} prime numbers between {a} and {b}.')
    #
    #
    # def get_all_prime(n):
    #     sieve = bytearray([True]) * (n // 2)
    #     for i in range(3, int(sqrt(n)) + 1, 2):
    #         if sieve[i // 2]:
    #             sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    #     return [2, *compress(range(3, n, 2), sieve[1:])]
    # Insert your code here
    for i in range(a, b + 1):
        if is_prime(i):
            number_of_primes_at_most_equal_to_b += 1
    if not number_of_primes_at_most_equal_to_b:
        print(f'There is no prime number beween {a} and {b}.')
    elif number_of_primes_at_most_equal_to_b == 1:
        print(f'There is a unique prime number beween {a} and {b}.')
    else:
        print(f'There are {number_of_primes_at_most_equal_to_b} prime numbers between {a} and {b}.')


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    return all(n % d for d in range(3, round(n ** 0.5) + 1, 2))


f(2, 2)
f(2, 3)
f(2, 5)
f(4, 4)
f(14, 16)
f(3, 20)
f(100, 800)
f(123, 456789)
