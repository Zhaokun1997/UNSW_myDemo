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
