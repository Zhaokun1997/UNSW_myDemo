# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3


import sys
from random import seed, randrange
from pprint import pprint
from collections import defaultdict

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}  # 生成的字典
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE


# TASK1
if keys:  # 若mapping中有key存在
    visited_flag = []  # 记录已经被访问过的key
    for key in mapping:  # 遍历mapping中每一个key
        value = mapping.get(key)
        # visited_flag的作用：防止重复性地找到子环
        if key in visited_flag:
            continue  # 遇到子环，则跳过
        # {4:4}
        if key == value:
            cycles.append([key])
            visited_flag.append(key)
        # {5:8,8:11,11:5}
        else:
            temp_item = [key, value]
            while value in mapping:  # 若有下一个 key
                new_key = value
                value = mapping.get(new_key)
                if value == temp_item[0]:  # 可以构成环的情况
                    cycles.append(temp_item)
                    visited_flag.extend(temp_item)  # extend()在列表末尾一次性追加另一个序列中的多个值
                    # for item in temp_item:
                    #     visited_flag.append(item)
                    break

                # 没有构成环时：
                # 有下面两种情况：
                # {7:5,5:8,8:11,11:5}环之外多余的尾巴元素 7：5
                if value in temp_item:
                    break

                # {3：9，9：1}之后没有后续
                temp_item.append(value)

# TASK2


# # METHOD 1
# reversed_dict = defaultdict(list)
# for key, value in mapping.items():
#     reversed_dict[value].append(key)
#     reversed_dict[value].sort()
#
# for key, value in reversed_dict.items():
#     length = len(value)
#     if length in reversed_dict_per_length:  # 若length存在在key中
#         reversed_dict_per_length[length].update({key: value})
#         # reversed_dict_per_length[length][key] = value
#     else:  # 若length不存在在key中
#         reversed_dict_per_length[length] = {}
#         reversed_dict_per_length[length].update({key: value})
#         # reversed_dict_per_length[length][key] = value
#         # reversed_dict_per_length[length] = {key: value}

# METHOD 2
reversed_dict = {}  # 翻转的字典
length_list = []  # 记录reversed_dict中所有value的长度

# 初始化翻转的字典，使得value的类型为list
for value in sorted(mapping.values()):
    reversed_dict[value] = []

# 填充元素
for key, value in mapping.items():
    reversed_dict[value].append(key)
    reversed_dict[value].sort()  # 对列表中的元素进行实时排序

# 构建length_list
for value in reversed_dict.values():
    length_list.append(len(value))
    length_list.sort()  # 对列表中的元素进行实时排序

# 将记录的每一个长度转换为集合：去除重复的长度value
length_set = set(length_list)
# 初始化reversed_dict_per_length
for length in length_set:
    reversed_dict_per_length[length] = {}

for key, value in reversed_dict.items():
    if len(value) in length_set:
        reversed_dict_per_length[len(value)].update({key: value})

# print(f'reversed_dict is : {reversed_dict}')
# print(f'length_list is : {length_list}')
# print(f'length_set is : {length_set}')


print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)
