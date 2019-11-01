# COMP9021 19T3 - Rachid Hamadi
# Quiz 5 *** Due Thursday Week 7
#
# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys


# 编码部分
def encode(list_of_integers):
    return_code = ''
    bin_list = []  # 对应的二进制转换列表
    for e in list_of_integers:
        bin_list.append(bin(e)[2:])
    # print('the corresponding bin_list is : ', bin_list)
    if len(bin_list) > 1:  # 列表中有大于一个元素
        for bin_number in bin_list:
            for letter in bin_number:
                return_code = return_code + (letter * 2)
            if bin_number == bin_list[-1]:  # 编码到最后一个元素则结束
                break
            return_code = return_code + '0'  # 每个元素之间编码时应该连接‘0’(按照规则)
        # print('after encode, the corresponding bin number is :', return_code)
        return int(return_code, 2)
    else:  # 列表中只有一个元素
        for letter in bin_list[0]:
            return_code = return_code + (letter * 2)
        # print('after encode, the corresponding bin number is :', return_code)
        return int(return_code, 2)


# 解码部分
def decode(integer):
    bin_value = bin(integer)[2:]
    if len(bin_value) == 1:  # 特殊case：1
        return None
    else:  # 输入的integer > 1时的情况
        result = ''  # 储存解码后的二进制数字
        i = 0
        while i < len(bin_value):
            try:
                if bin_value[i] == bin_value[i + 1]:  # 遇到‘00’或者‘11’时
                    result = result + bin_value[i]
                    # print(result)
                    i += 2
                else:
                    if bin_value[i] == '1':  # 遇到‘10’时(会浪费编码位数)
                        return None
                    else:  # 遇到‘01’时
                        i += 1
                        result = result + ','  # 遇到‘01’，跳过0，并记录下一个数字
                        # print(result)
            except IndexError:
                return None

        # print('after decoding, the result is :', result)
        temp_list = result.split(',')
        return_list = []
        for string in temp_list:
            return_list.append(int(string, 2))
        return return_list


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:  # 输入是整数-->判断并进行解码
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2:])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2:] for e in the_input)}]'
          )
    print('  It is encoded by', encode(the_input))
