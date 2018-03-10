# Problem 3
# What is the largest prime factor of the number 600851475143 ?

from helper_functions import factors
from helper_functions import is_prime

print(max(filter(lambda x: is_prime(x), factors(600851475143))))
