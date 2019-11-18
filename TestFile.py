# pair = [(1, 2), (2, 3)]
# with open('writeFile.tex', 'w') as file:
#     file.write(f'    \\draw {pair[0]} -- {pair[1]};')


# # 判断是否是闰年：
# input_year = input('please input a number as year')
# year = int(input_year)
#
# if year > 0:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print('this year is leap year.')
#     else:
#         print('this year is leap year.')


# 排列数字

num_list = [1, 2, 3, 4]


def permute(nums):
    from functools import reduce
    result = [list(i[:-1]) for i in
              reduce(lambda x, y: [str(a) + str(b) for a in x for b in y if str(b) not in str(a)], [nums] * len(nums))]

    return result


for i in permute(num_list):
    print(i)
