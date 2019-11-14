# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 3


'''
Will be tested with n at least equal to 2, and "not too large".
'''
from collections import defaultdict


def f(n):
    factors = defaultdict(int)
    # Insert your code here
    temp = n
    for i in range(2, n + 1):
        if temp == 1:
            break
        while temp % i == 0:
            factors[i] += 1
            temp = temp // i
    print(factors)
    print(f'The decomposition of {n} into prime factors reads:')
    print('  ', n, '=', end=' ')
    print(' x '.join(factors[x] == 1 and str(x) or f'{x}^{factors[x]}' for x in sorted(factors)))


f(2)
f(3)
f(4)
f(5)
f(6)
f(8)
f(10)
f(15)
f(100)
f(5432)
f(45103)
f(45100)
