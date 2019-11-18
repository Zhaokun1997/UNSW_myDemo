import sys

try:
    the_input = int(input('Please enter a number N:'))
except ValueError:
    print('Error, giving up')
    sys.exit()

# for i in range(2, the_input + 1):
#     divisor = []
#     for j in range(1, i // 2 + 1):
#         if i % j == 0:
#             divisor.append(j)
#     if sum(divisor) == i:
#         print(f'{i} is a perfect number.')

for i in range(2, the_input + 1):
    if sum(j for j in range(1, i // 2 + 1) if i % j == 0) == i:
        print(f'{i} is a perfect number.')
