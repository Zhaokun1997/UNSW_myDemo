# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 6


'''
You might find the zip() function useful, though you can also do without it.
'''

from random import randrange, seed
import itertools
from collections import Counter


def display(square, size):
    print('\n'.join(' '.join(f'{x:{size}}' for x in row) for row in square))


def f(for_seed, n, upper_bound):
    seed(for_seed)
    square = [[randrange(upper_bound) for _ in range(n)] for _ in range(n)]
    duplicates = set()
    ordered_square = [[]]
    print('Here is the square: ')
    display(square, len(str(upper_bound)))
    # Insert your code here
    duplicates = set([k for k, v in Counter(itertools.chain(*square)).items() if v > 1])

    if not duplicates:
        length = len(square)
        square = sorted(itertools.chain(*square))
        ordered_square = [square[i:i + length] for i in range(0, len(square), length)]
        ordered_square = zip(*ordered_square)


    # METHOD 2:
    # elements = []
    # for i in range(n):
    #     for j in range(n):
    #         if square[i][j] not in elements:
    #             elements.append(square[i][j])
    #         else:
    #             duplicates.add(square[i][j])
    # sort_list = []
    # for i in range(n):
    #     for j in range(n):
    #         sort_list.append(square[i][j])
    # sort_list.sort()
    # for i in range(1, n):
    #     ordered_square.append([])
    # for i in range(n):
    #     for j in range(n):
    #         ordered_square[j].append(sort_list[n * i + j])

    if duplicates:
        print('It is not a good square because it contains duplicates, namely: ', end='')
        print(' '.join(str(e) for e in sorted(duplicates)))
    else:
        print('It is a good square.')
        print('Ordering the elements from left to right column, from top to bottom, yields:')
        display(ordered_square, len(str(upper_bound)))
    print()


# f(0, 2, 2)
# f(0, 3, 5)
# f(0, 6, 50)
# f(0, 2, 50)
f(0, 3, 100)
# f(0, 6, 5000)
