# These are recurrent functions
from math import sqrt
from functools import reduce


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


def is_prime(n):
    if (n % 2 == 0 and n > 2) or n < 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
