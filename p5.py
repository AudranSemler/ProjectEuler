# Problem 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from helper_functions import prime_factorization, list_substraction_duplicates
from functools import reduce


def smallest_divisible(n):
    list_factors = prime_factorization(n)
    for i in range(n-1, 2, -1):
        potential_list = prime_factorization(i)
        new_factors = list_substraction_duplicates(list_factors, potential_list)
        list_factors.extend(new_factors)
    return reduce(lambda x, y: x * y, list_factors, 1)


print(smallest_divisible(20))
