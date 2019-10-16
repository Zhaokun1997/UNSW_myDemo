# COMP9021 19T3 - Rachid Hamadi
# Quiz 3 *** Due Thursday Week 4


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
# We start from a integer number based on 10;
# and convert this number into another one based on 8
# use the converted number as the procedure of steps
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys

# str类型的字符串，每个字符用字符本身或者\u1234，来表示都可以，后者则是直接是Unicode编码
# 但打印时都是打印字符本身

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()  # 移除字符串头尾指定的字符(此时是空格)
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
      )

# 有关进制转换：
# b：二进制，o：八进制，d：十进制，x：十六进制 <==> 对于format而言
# bin()、oct()、hex()返回值均为字符串，且分别带有0b、0o、0x前缀
print()

# INSERT YOUR CODE HERE

oct_number = '0' * nb_of_leading_zeroes + f'{int(code):o}'  # 八进制的数
reversed_list = list("".join(reversed(oct_number)))  # 反转之后的数->转换为列表
print(oct_number)
print(reversed_list)

# 向量字典
direct_map = {'0': (0, 1), '1': (1, 1), '2': (1, 0), '3': (1, -1), \
              '4': (0, -1), '5': (-1, -1), '6': (-1, 0), '7': (-1, 1)}

# 计步器(实时更新)
step_recording = {(0, 0): on}

# 当前的坐标值
current_x, current_y = 0, 0
for direction in reversed_list:
    current_x += direct_map[direction][0]
    current_y += direct_map[direction][1]
    if (current_x, current_y) in list(step_recording.keys()):  # 如果返回走过的地方
        del step_recording[(current_x, current_y)]  # 删除走过的地方
        continue
    step_recording[(current_x, current_y)] = on

# # for testing:
# for step in step_recording.items():
#     print(step)

print('\n')

# 用于记录所有 x,y 坐标的最大值和最小值
x_list = []
y_list = []
for each_step in step_recording.keys():
    x_list.append(each_step[0])
    y_list.append(each_step[1])

# 获取边界值（即：最大最小值）
if len(x_list) or len(y_list):
    max_x, min_x = max(x_list), min(x_list)
    max_y, min_y = max(y_list), min(y_list)

    # 填充地图的剩余部分为 ●
    for x_value in range(min_x, max_x + 1, 1):
        for y_value in range(min_y, max_y + 1, 1):
            if (x_value, y_value) in list(step_recording.keys()):
                continue
            step_recording[(x_value, y_value)] = off

    # for testing:
    for step in step_recording.items():
        print(step)

    for y_value in range(max_y, min_y - 1, -1):
        for x_value in range(min_x, max_x + 1, 1):
            print(step_recording[(x_value, y_value)], end=' ')
        print()
else:
    print()
