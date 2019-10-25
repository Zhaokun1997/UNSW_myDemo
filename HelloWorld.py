import re

x = 123
y = 321


# rules:当前作用域局部变量->外层作用域变量
# ->当前模块中的全局变量->python内置变量.
def testlocal():
    global x
    global y
    print(x + y)
    c = x + y
    print(c)
    print(x)


testlocal()
print(x)

a = 123


def outer():
    global a
    a = 100

    a1 = 200

    def inter():
        nonlocal a1
        a1 = 300

    inter()
    print(a1)
    pass


outer()
print(a)

dic = [3, 5, 7, 6, 1, 0, 2]
d = [{"order": 3}, {"order": 1}, {"order": 2}]

while True:
    roman_number = input("input a roman number : ")
    upper = roman_number.upper()
    pattern_roman = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
    match_obj = pattern_roman.match(upper)
    if match_obj:
        print(upper)
        print('input is valid.')
    else:
        print(upper)
        print('input is invalid.')

