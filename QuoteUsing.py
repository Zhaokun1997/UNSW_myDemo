# tape = [0, 0, 1, 1, 1, 0]
# E = (str(item) for item in tape)  # 迭代器
#
#
# def draw_horizontal_line():
#     global tape
#     print('-' * (2 * len(tape) + 1))
#
#
# def display_tape():
#     global E
#     draw_horizontal_line()
#     print('|' + '|'.join(E) + '|')
#     draw_horizontal_line()
#     return None
#
# display_tape()

# myFile = open('addition.txt', 'r')
# lines = myFile.readlines()
# for line in lines:
#     print(line, end='')
#
# for line in myFile:
#     print(line, end='')


# # 左闭右开的区间
# str1 = 'abcdefg\n'
# def testIndex():
#     print(str1[0:])
#     print(str1[:len(str1)])
#     print(str1[:len(str1)-1])
#     print(str1[0:-1])
#     print(str1[:-1])
# testIndex()



dic = {1: 'A', 2: 'B', 4: 'D'}
del dic[1]
print(dic)
