from math import sqrt


# verify if a number n is prime
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