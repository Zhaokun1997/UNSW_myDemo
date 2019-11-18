from itertools import combinations

two_digits = []
for i in range(10, 100):
    two_digits.append(str(i))

for row in combinations(two_digits, 3):
    temp = ''
    product = 1
    for i in range(len(row)):
        temp += row[i]
        product *= int(row[i])
    if len(set(temp)) != len(temp):
        continue
    if set(temp) != set(str(product)):
        continue
    print(' x '.join(row[i] for i in range(len(row))) + ' = ' + f'{str(product)}')
