# [100, 999]
sum_of_square_integer = [None] * 1_000

# 32 ** 32 is more than 3 digits
upper_square = 32


def nb_of_consecutive(n):
    if not sum_of_square_integer[n]:
        return 0
    if not sum_of_square_integer[n + 1]:
        return 1
    if not sum_of_square_integer[n + 2]:
        return 2
    return 3


for i in range(upper_square):
    for j in range(upper_square):
        n = i ** 2 + j ** 2
        if n < 100:
            continue
        elif n >= 1_000:
            break
        if not sum_of_square_integer[n]:
            sum_of_square_integer[n] = i, j

for num in range(100, 1_000 - 3):
    nb = nb_of_consecutive(num)
    if nb >= 3:
        print(f'({num}, {num + 1}, {num + 2})'
              f'(equal to ({sum_of_square_integer[num][0]}^2+{sum_of_square_integer[num][1]}^2, '
              f'{sum_of_square_integer[num + 1][0]}^2+{sum_of_square_integer[num + 1][1]}^2, '
              f'{sum_of_square_integer[num + 2][0]}^2+{sum_of_square_integer[num][1]}^2))'
              f' is a solution.')
