try:
    height = int(input('please input a integer as height'))
    if height <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input!')

index = 0
for i in range(1, height + 1):
    space = ' ' * (height - i)
    str_list = []
    j = 0
    while j < i:
        if index == 26:
            index = 0
        sym = chr(65 + index)
        str_list.append(sym)
        j += 1
        index += 1
    print(space, end='')
    for m in range(len(str_list)):
        print(f'{str_list[m]}', end='')
    for n in range(-2, -len(str_list) - 1, -1):
        print(f'{str_list[n]}', end='')
    print()
