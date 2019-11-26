# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 2


'''
You might find the function bin() useful.
Will be tested with n a strictly positive integer.
'''

import sys


def f(n):
    # Insert your code here
    num = bin(n)[2:]
    l = list(str(num))
    count = l.count('1')
    print(f'{n} in binary reads as: {num}.')
    if count == 1:
        print(f'Only one bit is set to 1 in the binary representation of {n}.')
    else:
        print(f'{count} bits are set to 1 in the binary representation of {n}.')
    print()


f(1)
f(2)
f(3)
f(7)
f(2134)
f(9871)
