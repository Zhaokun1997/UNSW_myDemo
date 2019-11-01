# COMP9021 19T3 - Rachid Hamadi
# Quiz 7 *** Due Thursday Week 9
#
# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).


from random import seed, randrange
import sys
from collections import defaultdict

dim = 10
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 方向：上左下右


def display_grid():
    for row in grid:
        print('   ', *row)

    # Returns the number of shapes we have discovered and "coloured".


# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.
def colour_shapes():
    color_index = 2
    cp_grid = [x[:] for x in grid]
    for i in range(len(cp_grid)):
        for j in range(len(cp_grid[i])):
            if cp_grid[i][j] == 1:  # 如果还没有被染色（即：还是 1 时）
                find_shapes(i, j, color_index, cp_grid)
                color_index += 1  # 染色完毕之后换颜色
    # 以上染色完毕
    # print()
    # display_new_grid(cp_grid)

    # 记录所有的染色组
    all_shapes = defaultdict(list)
    for i in range(len(cp_grid)):
        for j in range(len(cp_grid[i])):
            if cp_grid[i][j] > 1:
                all_shapes[cp_grid[i][j]].append((i, j))

    # for item in all_shapes.items():
    #     print('   ', item)
    strikes = []
    for color_key in all_shapes:
        strike = 0
        if 0 < len(all_shapes[color_key]) <= 2:  # 对于每一个 0<size<=2 的shape, 不予理睬
            strikes.append(strike)
            continue
        else:
            for x, y in all_shapes[color_key]:
                count_neighbor_1 = 0
                for x_dir, y_dir in direction:
                    if 0 <= x + x_dir < dim and 0 <= y + y_dir < dim \
                            and cp_grid[x + x_dir][y + y_dir] == cp_grid[x][y]:
                        count_neighbor_1 += 1
                if count_neighbor_1 == 1:
                    # print((x, y))
                    strike += 1
        strikes.append(strike)
    return strikes
    # print(strikes)


def max_number_of_spikes(num_of_shapes):
    max_number = max(num_of_shapes)
    return max_number


# Replace pass above with your code


# 找 shape，然后进行染色
def find_shapes(i, j, color, cp_grid):
    if 0 <= i < dim and 0 <= j < dim and cp_grid[i][j] == 1:
        cp_grid[i][j] = color
        for x, y in direction:
            find_shapes(i + x, j + y, color, cp_grid)  # 递归染色
    else:
        return


# 输出 copy 的矩阵
def display_new_grid(new_grid):
    for row in new_grid:
        print('   ', *row)



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
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
      )
