# COMP9021 19T3 - Rachid Hamadi
# Quiz 6 *** Due Thursday Week 8
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111


from random import seed, randrange
import sys

dim = 10


def display_grid():
    for row in grid:
        print('   ', *row)


def size_of_largest_parallelogram():
    # print('\nvertical')
    max_vertical = find_max_size_vertical()
    # print('\nleft')
    max_left = find_max_size_left()
    # print('\nright')
    max_right = find_max_size_right()
    return max(max_vertical, max_left, max_right)


# POSSIBLY DEFINE OTHER FUNCTIONS
def display_new_grid(new_grid):
    for row in new_grid:
        print('   ', *row)


# 平行四边形垂直分析
# 111
# 111
# 111
# 111
def find_max_size_vertical():
    vertical_grid = [x[:] for x in grid]
    size_record = []  # 对于每行数据而言的所能构成的最大的平行四边形
    for i in range(len(vertical_grid)):
        for j in range(len(vertical_grid[i])):
            if i > 0:
                if vertical_grid[i][j] == 1:
                    vertical_grid[i][j] = vertical_grid[i][j] + vertical_grid[i - 1][j]
                else:
                    pass
        for j in range(len(vertical_grid[i])):
            temp_j = j
            temp = []
            while temp_j < len(vertical_grid[i]) and vertical_grid[i][temp_j] > 1:
                temp.append(vertical_grid[i][temp_j])
                temp_j += 1
            if len(temp) == 0 or len(temp) == 1:
                continue
            else:
                temp_size = []
                for k in range(2, len(temp) + 1):
                    temp_size.append(min(temp[:k]) * len(temp[:k]))
                size_record.append(max(temp_size))
    # display_new_grid(vertical_grid)
    return_value = 0
    if len(size_record):
        return_value = max(size_record)
    return return_value


# 平行四边形向左分析
#    111
#   111
#  111
# 111
def find_max_size_left():
    left_grid = [x[:] for x in grid]
    size_record = []
    for i in range(len(left_grid)):
        for j in range(len(left_grid[i])):
            if i > 0:
                if left_grid[i][j] == 1:
                    try:
                        left_grid[i][j] = left_grid[i][j] + left_grid[i - 1][j + 1]
                    except IndexError:
                        pass
                else:
                    pass
        for j in range(len(left_grid[i])):
            temp_j = j
            temp = []
            while temp_j < len(left_grid[i]) and left_grid[i][temp_j] > 1:
                temp.append(left_grid[i][temp_j])
                temp_j += 1
            if len(temp) == 0 or len(temp) == 1:
                continue
            else:
                temp_size = []
                for k in range(2, len(temp) + 1):
                    temp_size.append(min(temp[:k]) * len(temp[:k]))
                size_record.append(max(temp_size))
    # display_new_grid(left_grid)
    return_value = 0
    if len(size_record):
        return_value = max(size_record)
    return return_value


# 平行四边形向右分析
# 111
#  111
#   111
#    111
def find_max_size_right():
    right_grid = [x[:] for x in grid]
    size_record = []
    for i in range(len(right_grid)):
        for j in range(len(right_grid[i])):
            if i > 0 and j > 0:
                if right_grid[i][j] == 1:
                    try:
                        right_grid[i][j] = right_grid[i][j] + right_grid[i - 1][j - 1]
                    except IndexError:
                        pass
                else:
                    pass
        for j in range(len(right_grid[i])):
            temp_j = j
            temp = []
            while temp_j < len(right_grid[i]) and right_grid[i][temp_j] > 1:
                temp.append(right_grid[i][temp_j])
                temp_j += 1
            if len(temp) == 0 or len(temp) == 1:
                continue
            else:
                temp_size = []
                for k in range(2, len(temp) + 1):
                    temp_size.append(min(temp[:k]) * len(temp[:k]))
                size_record.append(max(temp_size))
    # display_new_grid(right_grid)
    return_value = 0
    if len(size_record):
        return_value = max(size_record)
    return return_value


try:

    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                               ).split()
                         )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
        for _ in range(dim)
        ]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
          )
else:
    print('There is no parallelogram with horizontal sides.')
