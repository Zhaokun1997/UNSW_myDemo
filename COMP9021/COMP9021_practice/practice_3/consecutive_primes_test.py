from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n > 2:
        if n % 2 == 0:  # n is even
            return False
        else:  # n is odd
            return all(n % d for d in range(3, round(sqrt(n)) + 1, 2))


good_leap = tuple(sum(i for i in range(0, k, 2)) for k in range(2, 13, 2))
print(good_leap)

for num in range(10_001, 100_000):
    if all(((i in good_leap) == (is_prime(num + i))) for i in range(0, good_leap[-1] + 1, 2)):
        print(f'  '.join(str(num + i) for i in good_leap))
