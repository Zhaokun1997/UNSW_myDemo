import sys
from math import sqrt
from itertools import compress


def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(sqrt(n))+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n - i*i-1)//(2 * i) + 1)
            
    result =  [2, *compress(range(3, n, 2), sieve[1:])]
    largest_prime_strictly_smaller_than_n = result[-1]
    print(f'The largest prime strictly smaller than {n} is {largest_prime_strictly_smaller_than_n}.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
