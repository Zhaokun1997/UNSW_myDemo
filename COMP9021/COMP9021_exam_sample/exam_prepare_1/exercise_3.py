from collections import defaultdict


def single_factors(number):
    factors = defaultdict(int)
    temp = number
    for i in range(2, number + 1):
        if temp == 1:
            break
        while temp % i == 0:
            factors[i] += 1
            temp = temp // i
    product = 1
    for key in factors:
        product *= key
    return product


print(single_factors(2))
print(single_factors(4096))
print(single_factors(85))
print(single_factors(10440125))
print(single_factors(154))
print(single_factors(52399401037149926144))
