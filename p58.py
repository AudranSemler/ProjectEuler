# Problem 58
# what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

from helper_functions import is_prime
from math import sqrt

diagonal_numbers = 5
num_primes = 3
head = 9
step = 2

while (num_primes / diagonal_numbers) > 0.1:
    step += 2
    for i in range(0, 3):
        head += step
        if is_prime(head):
            num_primes += 1
    head += step
    diagonal_numbers += 4
print(int(sqrt(head)))