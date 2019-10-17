import sys
import re

roman_symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
pattern_roman = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')  # 罗马数字的匹配模式


# 判断是否为合法的可转换为罗马数字的正整数
def is_valid_positiveInt(string):
    if string.isdigit() and (not string.startswith('0')):
        if int(string) <= 3999:
            return True
        else:
            return False
    return False


# 判断是否为合法的罗马数字
def is_roman(string):
    upper_str = string.upper()
    for letter in upper_str:
        if letter not in roman_symbol:
            return False
    match_roman = pattern_roman.match(upper_str)
    if match_roman:
        return True
    return False


# feedback 字符串列表
feedback_str = ["I don't get what you want, sorry mate!", \
                "Hey, ask me something that's not impossible to do! ", \
                "Sure! It is "]
while 1:
    user_input = input('How can I help you?')
    match_obj = re.match(r'Please convert (.*)', user_input)  # 匹配输入的字符串是否符合条件

    try:
        if match_obj:  # 测试输入的字符串是否符合基本条件
            group1 = match_obj.group(1)  # 提取出 *** 的部分
            # print(group1)
            match_obj_second = re.search(r'(.*) using (.*)', group1)
            match_obj_third = re.search(r'(.*) minimally', group1)
            if match_obj_second:  # 满足第二种输入条件
                ####
                ####
                ####
                ####
                ####
                ####
                if (match_obj_second.group(1).isnumeric() or is_roman(match_obj_second.group(1))) \
                        and (match_obj_second.group(2).isnumeric() or is_roman(match_obj_second.group(2))):
                    print(match_obj_second.group(1))
                    print(match_obj_second.group(2))
            elif match_obj_third:  # 满足第三种输入条件
                ####
                ####
                ####
                ####
                ####
                ####
                ####
                if match_obj_third.group() != group1:
                    print()
                print(match_obj_second.group(1))
            else:  # 只满足第一种输入条件
                if is_valid_positiveInt(group1):  # Arabic转换成Roman(按位数切分，分别匹配)
                    num = int(group1)
                    convert_map = {0: ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
                                   1: ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'LC'),
                                   2: ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
                                   3: ('', 'M', 'MM', 'MMM')}
                    roman = list()
                    roman.append(convert_map[3][num // 1000])
                    roman.append(convert_map[2][num // 100 % 10])
                    roman.append(convert_map[1][num // 10 % 10])
                    roman.append(convert_map[0][num % 10])
                    result = ''
                    for element in roman:
                        result += element
                    print(feedback_str[2], result)
                elif is_roman(group1):  # Roman转换成Arabic(右加左减原则)
                    weight_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, \
                                  'C': 100, 'D': 500, 'M': 1000}
                    result = 0
                    for i in range(len(group1) - 1):
                        if weight_map[group1[i]] < weight_map[group1[i + 1]]:
                            result -= weight_map[group1[i]]
                        else:
                            result += weight_map[group1[i]]
                    result += weight_map[group1[-1]]
                    print(feedback_str[2], result)
                else:
                    print(feedback_str[1])

        else:
            print(feedback_str[0])
    except ValueError:
        print("Invaild input!")
        sys.exit()
