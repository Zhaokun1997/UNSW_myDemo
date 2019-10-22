import sys
import re
from collections import OrderedDict

roman_symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
pattern_roman = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')  # 罗马数字的匹配模式


def find_once(word, string):
    count = 0
    for e in string:
        if word == e:
            count += 1
    if count == 1:
        return True
    else:
        return False


# 验证字符串匹配
def match(pattern, map):
    key = 1
    while key <= len(map):
        if pattern == map[key][1]:
            return key
        else:
            key += 1
            continue

    return -1


# 获取字符串模式
def get_index(string):
    return [string.index(letter) for letter in string]


# 用给定的字母创建罗马数字权值表
def create_weightMap(string):
    roman_weight_map = OrderedDict()
    list_str = list(string)
    list_str.reverse()
    for index in range(len(list_str)):
        if index == 0:
            roman_weight_map[list_str[index]] = 1
        elif index == 1:
            roman_weight_map[list_str[index]] = 5
        elif index > 1 and index % 2 == 0:
            roman_weight_map[list_str[index]] = roman_weight_map[list_str[index - 1]] * 2
        else:
            roman_weight_map[list_str[index]] = roman_weight_map[list_str[index - 1]] * 5
    # print('generated roman weight map is :', roman_weight_map)
    return roman_weight_map


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


# 罗马数字转换为整数
def roman_convert_to_integer(weightMap, converting_number):
    returnValue = 0
    for i in range(len(converting_number) - 1):
        if weightMap[converting_number[i]] < weightMap[converting_number[i + 1]]:
            returnValue -= weightMap[converting_number[i]]
        else:
            returnValue += weightMap[converting_number[i]]
    returnValue += weightMap[converting_number[-1]]
    return returnValue


# feedback 字符串列表
feedback_str = ["I don't get what you want, sorry mate!", \
                "Hey, ask me something that's not impossible to do!", \
                "Sure! It is"]

user_input_initial = input('How can I help you?')
user_input_initial.strip()  # 消除前后空格
user_input = user_input_initial.split()
input_length = len(user_input)
if input_length not in [3, 4, 5]:
    print(feedback_str[0])
    sys.exit()

try:
    if user_input[0] == 'Please' and user_input[1] == 'convert':
        # the first kind of input
        if len(user_input) == 3:
            if is_valid_positiveInt(user_input[2]):  # Arabic转换成Roman(按位数切分，分别匹配)
                num = int(user_input[2])
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
            elif is_roman(user_input[2]):  # Roman转换成Arabic(右加左减原则)
                weight_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, \
                              'C': 100, 'D': 500, 'M': 1000}
                result = roman_convert_to_integer(weight_map, user_input[2])
                print(feedback_str[2], result)
            else:
                print(feedback_str[1])

        # the third kind of input
        elif len(user_input) == 4:
            if user_input[3] == 'minimally':
                if user_input[2].isalpha():
                    converting_letter = user_input[2]
                    alphabet = []
                    for i in range(-1, -len(converting_letter) - 1, -1):
                        if converting_letter[i] not in alphabet:
                            alphabet.append(converting_letter[i])
                        else:
                            if converting_letter[i] != converting_letter[i + 1]:
                                if converting_letter[i] == converting_letter[i + 2]:
                                    index = alphabet.index(converting_letter[i])
                                    if index % 2 == 0:
                                        alphabet[index] = alphabet[index + 1]
                                        alphabet[index + 1] = '_'
                                        alphabet.append(converting_letter[i])
                                    elif index == len(alphabet) - 1:
                                        alphabet[index] = '_'
                                        alphabet.append(converting_letter[i])
                                    else:
                                        alphabet[index] = '_'
                                        alphabet.append('_')
                                        alphabet.append(converting_letter[i])
                                elif i + 3 < 0 and converting_letter[i] == converting_letter[i + 3] != \
                                        converting_letter[i + 2]:
                                    index = alphabet.index(converting_letter[i])
                                    if index % 2 == 1:
                                        alphabet[index] = '_'
                                        alphabet.append(converting_letter[i])
                                        alphabet.append(alphabet[index + 2])
                                        alphabet[index + 2] = '_'
                                    else:
                                        alphabet.append(alphabet[index + 2])
                                        alphabet[index + 2] = converting_letter[i]
                                        alphabet[index] = alphabet[index + 1]
                                        alphabet[index + 1] = '_'
                            elif converting_letter[i] == converting_letter[i + 1]:
                                index = alphabet.index(converting_letter[i])
                                if index % 2 == 1:
                                    alphabet.append(converting_letter[i])
                                    alphabet[index] = '_'
                    for i in range(len(alphabet)):
                        if len(alphabet) > 1 and i % 2 == 1:
                            if find_once(alphabet[i], converting_letter) \
                                    and find_once(alphabet[i - 1], converting_letter):
                                alphabet[i], alphabet[i - 1] = alphabet[i - 1], alphabet[i]
                    alphabet.reverse()
                    weight_alph = ''.join(alphabet)
                    weight_number = 1
                    weight = list()
                    weight.append(weight_number)
                    for num in range(1, len(alphabet)):
                        if num % 2 == 1:
                            weight_number = weight_number * 5
                        else:
                            weight_number = weight_number * 2
                        weight.append(weight_number)
                    weight.reverse()
                    # print('weight_alph is : ', weight_alph)
                    # print('weight_number is : ', weight)
                    weight_map = {}
                    for i in range(len(weight_alph)):
                        weight_map[weight_alph[i]] = weight[i]
                    result = roman_convert_to_integer(weight_map, converting_letter)
                    print(f'{feedback_str[2]} {result} using {weight_alph}')
                else:
                    print(feedback_str[1])
            else:
                print(feedback_str[0])

        # the second kind of input
        elif len(user_input) == 5:
            if user_input[3] == 'using':
                # 判断第一个***是否满足条件
                converting_letter = user_input[2]
                provided_letter = user_input[4]
                A = converting_letter.isalpha() \
                    or (converting_letter.isdigit() and (not converting_letter.startswith('0')))
                # 判断第二个***是否满足条件
                B = len(provided_letter) == len(set(provided_letter)) \
                    and provided_letter.isalpha()
                if A and B:
                    weight_map = create_weightMap(provided_letter)  # 生成权值罗马字母表
                    if converting_letter.isdigit():  # 需要被转换的***为数字时
                        number = int(converting_letter)
                        convert_map = {}
                        max_power = 0
                        while number // (10 ** max_power) > 0:
                            max_power += 1
                        # print('max_power is : ', max_power)
                        convert_keys = list(weight_map.keys())
                        # print('convert_keys is : ', convert_keys)
                        j = 0
                        for i in range(max_power):
                            if j + 2 < len(convert_keys):
                                convert_map[i] = (
                                    '', convert_keys[j], convert_keys[j] * 2, convert_keys[j] * 3,
                                    convert_keys[j] + convert_keys[j + 1], convert_keys[j + 1],
                                    convert_keys[j + 1] + convert_keys[j],
                                    convert_keys[j + 1] + convert_keys[j] * 2,
                                    convert_keys[j + 1] + convert_keys[j] * 3,
                                    convert_keys[j] + convert_keys[j + 2])
                            elif j + 1 < len(convert_keys):
                                convert_map[i] = (
                                    '', convert_keys[j], convert_keys[j] * 2, convert_keys[j] * 3,
                                    convert_keys[j] + convert_keys[j + 1], convert_keys[j + 1],
                                    convert_keys[j + 1] + convert_keys[j],
                                    convert_keys[j + 1] + convert_keys[j] * 2,
                                    convert_keys[j + 1] + convert_keys[j] * 3)
                            elif j < len(convert_keys):
                                convert_map[i] = (
                                    '', convert_keys[j], convert_keys[j] * 2, convert_keys[j] * 3)
                            j += 2
                        # print(convert_map)
                        roman = list()
                        # print('the number is :', number)
                        if number // (10 ** max(list(convert_map.keys()))) > 10:  # 数字大于所给定的序列权值
                            print(feedback_str[1])
                        else:  # 数字可以用所给定的序列权值表示
                            for i in range(max_power - 1, -1, -1):
                                if i == max_power - 1:
                                    roman.append(convert_map[i][number // (10 ** i)])
                                else:
                                    roman.append(convert_map[i][number // (10 ** i) % 10])
                            result = ''
                            for element in roman:
                                result += element
                            print(feedback_str[2], result)
                    else:  # 需要被转换的***为罗马字符时
                        keys = list(weight_map.keys())
                        length = len(keys)
                        compile_str = '^'
                        if (length % 2) == 1:  # length是奇数
                            key_i = length - 1
                            compile_str += keys[key_i] + '{0,3}'
                            key_i -= 2
                            while key_i >= 0:
                                compile_str += '(' + keys[key_i] + keys[key_i + 2] + '|' + keys[key_i] + keys[
                                    key_i + 1] \
                                               + '|' + keys[key_i + 1] + '?' + keys[key_i] + '{0,3}' + ')'
                                key_i -= 2
                            compile_str += '$'
                            # print('compile_str is : ', compile_str)
                            pattern = re.compile(r'' + compile_str + '')
                            m_obj = pattern.match(converting_letter)
                            if m_obj:
                                result = roman_convert_to_integer(weight_map, converting_letter)
                                print(feedback_str[2], result)
                            else:
                                print(feedback_str[1])
                        else:  # length是偶数
                            key_i = length - 1  # D
                            if key_i >= 1:
                                compile_str += '(' + keys[key_i - 1] + keys[key_i] \
                                               + '|' + keys[key_i] + '?' + keys[key_i - 1] + '{0,3}' + ')'
                                key_i -= 3
                            while key_i >= 0:
                                compile_str += '(' + keys[key_i] + keys[key_i + 2] + '|' + keys[key_i] + keys[
                                    key_i + 1] \
                                               + '|' + keys[key_i + 1] + '?' + keys[key_i] + '{0,3}' + ')'
                                key_i -= 2
                            compile_str += '$'
                            # print('compile_str is : ', compile_str)
                            pattern = re.compile(r'' + compile_str + '')
                            m_obj = pattern.match(converting_letter)
                            if m_obj:
                                result = roman_convert_to_integer(weight_map, converting_letter)
                                print(feedback_str[2], result)
                            else:
                                print(feedback_str[1])
                else:
                    print(feedback_str[1])
            else:
                print(feedback_str[0])

    else:
        print(feedback_str[0])
except Exception:
    print(feedback_str[0])
    sys.exit()
