try:
    N = int(input('Enter a nonnegative integer: '))
    if N < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, try again')

pascal_tri = [[1] * (n + 1) for n in range(N + 1)]

for n in range(2, N + 1):
    for k in range(1, n // 2 + 1):
        pascal_tri[n][k] = pascal_tri[n - 1][k - 1] + pascal_tri[n - 1][k]
    for k in range(n // 2 + 1, n):
        pascal_tri[n][k] = pascal_tri[n - 1][k - 1] + pascal_tri[n - 1][k]

width = len(str(pascal_tri[N][N // 2]))
for n in range(0, N + 1):
    print(' ' * width * (N - n), end='')
    print((' ' * width).join(f'{pascal_tri[n][k]:{width}}' for k in range(len(pascal_tri[n]))))
