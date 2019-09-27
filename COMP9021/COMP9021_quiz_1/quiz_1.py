# COMP9021 19T3 - Rachid Hamadi
# Quiz 1 *** Due Thursday Week 2


import sys
from random import seed, randrange

# seed()改变随机数生成器的种子，相同的种子生成的下一个随机数相同
# randrange()返回指定递增基数集合中的一个随机数，基数默认值为1
# randrange(0,100, 2) range:[0,100)  # 从0-100中随机选取一个偶数

try:
    # 使用绝对值的原因是 range(0,3) is 0,1,2
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}  # 生成的字典
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)

mapping_as_a_list = []
one_to_one_part_of_mapping = {}
nonkeys = []

# INSERT YOUR CODE HERE
# TASK1
keys_number = len(mapping)  # key的数量

# TASK2
keys = list()  # 提取 mapping 里面存在的key到keys
for key in list(mapping.keys()):
    keys.append(key)  # 提取对应的key
for i in range(1, upper_bound):  # 找出不是key的集合
    if i not in keys:
        nonkeys.append(i)

# TASK3
for index in range(upper_bound):
    mapping_as_a_list.append(None)  # 初始化元素都是None
    if index in keys:
        mapping_as_a_list[index] = mapping[index]

# TASK4
# METHOD1
one_to_one_part_of_mapping = {key: value for key, value in mapping.items() \
                              if list(mapping.values()).count(value) == 1}


# METHOD2
# for key1, value1 in mapping.items():
#     count = 0
#     for key2, value2 in mapping.items():
#         if value1 == value2:
#             count += 1
#     if count == 1:
#         one_to_one_part_of_mapping[key1] = value1

# METHOD3
# one_to_one_part_of_mapping = mapping.copy()  # 复制原始的mapping字典
# for key1 in list(mapping.keys()):
#     for key2 in list(mapping.keys()):
#         if mapping[key1] == mapping[key2] and key1 != key2:
#             try:
#                 one_to_one_part_of_mapping.pop(key1)
#                 one_to_one_part_of_mapping.pop(key2)
#             except KeyError:
#                 print('there is a key error!')
#                 pass

print()
print('the mappings\'s so-called "keys" make up a set whose number of elements is ', keys_number)
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.
one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                              for key in sorted(one_to_one_part_of_mapping)
                              }
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)
