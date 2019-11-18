import sys
from itertools import combinations


def solve(available_digits, desired_sum):
    if desired_sum < 0:
        return 0
    if available_digits == 0:
        if desired_sum == 0:
            return 1
        return 0

    return solve(available_digits // 10, desired_sum) + solve(available_digits // 10,
                                                              desired_sum - available_digits % 10)


try:
    available_digits = abs(int(input('Input a number that we will use as available digits: ')))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    desired_sum = int(input('Input a number that represents the desired sum: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


# METHOD_2 : USING COMBINATION METHOD
# available_lst = [int(num) for num in available_digits]
# result_lst = []
#
# for i in range(1, len(available_lst) + 1):
#     for lst in combinations(available_lst, i):
#         if sum(lst) == desired_sum:
#             result_lst.append(lst)
# nb_solutions = len(result_lst)
# for lst in result_lst:
#     print(lst)
# print(f'There are {nb_solutions} solutions.')

nb_solutions = solve(available_digits, desired_sum)
print(f'There are {nb_solutions} solutions.')
