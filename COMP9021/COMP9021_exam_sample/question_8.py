# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 8


'''
Will be tested with letters a string of DISTINCT UPPERCASE letters only.
'''
from itertools import permutations as pm


def find_sub_match(letters):
    pass


def f(letters):
    dictionary = 'dictionary.txt'
    solutions = []
    # Insert your code here
    dic_letter = []
    with open(dictionary, 'r') as file:
        # 读取字典
        lines = file.readlines()
        min_len = 100
        max_len = 1
        for line in lines:
            row = line.strip()
            dic_letter.append(row)
            if len(row) < min_len:
                min_len = len(row)
            if len(row) > max_len:
                max_len = len(row)
        print(dic_letter)
        print(min_len, max_len)
        # 开始匹配
        for i in range(min_len, max_len + 1):
            for item in pm(letters, i):
                temp_letters = letters
                match = ''.join(str(i) for i in item)
                temp = []
                while match in dic_letter:
                    temp.append(match)
                    # 去掉先匹配的子串
                    for letter in item:
                        if temp_letters:
                            temp_letters.remove(letter)

    if not solutions:
        print('There is no solution')
    else:
        print(f'The pairs of words using all (distinct) letters in "{letters}" are:')
        for solution in solutions:
            print(solution)


# f('ABCDEFGH')
# f('GRIHWSNYP')
f('ONESIX')
# f('UTAROFSMN')
