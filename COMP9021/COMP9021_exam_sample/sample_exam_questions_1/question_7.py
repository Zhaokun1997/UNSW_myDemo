# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 7


def f(height):
    # Insert your code here
    num = 0
    # 1 2 3 4
    sep = height - 1
    print(f'f({height}) result is : ')
    for h in range(1, height + 1):
        pre = ' ' * sep
        sep -= 1
        print(pre, end='')
        for i in range(2 * h - 1):
            print(num % 10, end='')
            num += 1
        print()


f(1)
f(2)
f(3)
f(4)
f(5)
f(6)
f(20)
