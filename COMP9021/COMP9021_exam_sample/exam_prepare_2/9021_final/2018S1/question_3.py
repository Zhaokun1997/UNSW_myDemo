from math import sqrt
import sys


def f(n, d):
    '''
    >>> f(2, 1)
    1 is not a proper factor of 2.
    >>> f(2, 2)
    2 is not a proper factor of 2.
    >>> f(16, 2)
    2 is a proper factor of 16 of mutiplicity 4.
    >>> f(100, 20)
    20 is a proper factor of 100 of mutiplicity 1.
    >>> f(8 ** 7 * 3 ** 5 * 11 ** 2, 8)
    8 is a proper factor of 61662560256 of mutiplicity 7.
    >>> f(3 ** 3 * 11 * 13 ** 2 * 40 ** 6, 8)
    8 is a proper factor of 205590528000000 of mutiplicity 6.
    '''
    if n > 1 and d == 1 or n == d:
        print(f'{d} is not a proper factor of {n}.')
    else:
        m = n
        power = 0
        while n % d == 0:
            power += 1
            n = n // d

        print(f'{d} is a proper factor of {m} of mutiplicity {power}.')


if __name__ == '__main__':
    import doctest

    doctest.testmod()
