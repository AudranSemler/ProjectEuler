# These are recurrent functions
from math import sqrt, log, floor
from functools import reduce


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


def prime_factorization(n):
    res = []
    while n%2 == 0:
        res.append(2)
        n = int(n / 2)
    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            res.append(i)
            n = int(n / i)
    if n > 2:
        res.append(n)
    return res


def is_prime(n):
    if (n % 2 == 0 and n > 2) or n < 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    return str(n) == str(n)[::-1]


# returns elements in list2 that are not in list1, with counting
# This is NOT a set difference
def list_substraction_duplicates(list1, list2):
    res = []
    l1 = list1[:]

    for item in list2:
        if item in l1:
            l1.remove(item)
        else:
            res.append(item)

    return res


def binomial_coefficient(n, k):
    c = [0 for i in range(k + 1)]
    c[0] = 1

    for i in range(1, n + 1):
        j = min(i, k)
        while j > 0:
            c[j] = c[j] + c[j - 1]
            j -= 1

    return c[k]
