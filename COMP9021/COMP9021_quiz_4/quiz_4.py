# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.


import sys

lower_alpha = list(map(chr, range(97, 123)))
upper_alpha = list(map(chr, range(65, 91)))
Alpha = lower_alpha + upper_alpha
Alpha.extend([',', ' ', '_'])


def check_symbol(str_value):
    for letter in str_value:
        # if (letter in ['(', ')']) or \
        #         (not (letter.isalpha() or (letter is '_'))):  # 如果存在括号或者不是字母以及下划线，则不符合 0 参数条件
        if letter not in Alpha:
            return False
    return True


# arity is the number of parameters
# word is consisting of nothing but alphabetic characters and underscores
def is_valid(word_input, num_para):
    word_input = word_input.replace(' ', '')  # 去掉所有的空格
    if num_para == 0:  # 参数个数为 0 的情况（不允许有括号存在）
        return check_symbol(word_input)

    else:  # 参数个数＞ 0 的情况（不允许有括号存在）
        word_input = word_input.replace(',', ' ')  # 去掉所有的空格
        word_input = word_input.replace('(', ' ( ')  # 替换括号为括号左右加空格
        word_input = word_input.replace(')', ' ) ')
        # print('word : ', word)
        word_input = word_input.split()  # 默认分割全部所有的“空”字符
        # print('after split word : ', word)
        if word_input.count('(') != word_input.count(')'):  # 左右括号的数量不同，则不符合
            return False
        else:  # 左右括号相同时
            stack = []
            for element in word_input:
                stack.append(element)  # 持续入栈
                if element == ')':  # 当匹配到右括号时，计算括号内的元素数量
                    count = 0
                    while len(stack) > 0:  # 持续出栈
                        temp = stack.pop()
                        if temp != '(':  # 计算括号内的元素数量
                            count += 1
                        else:  # 若匹配到左括号，则跳出局部计算区域
                            break
                    if count != num_para + 1:
                        return False
            return True

    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')
