# Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.

from helper_functions import is_palindrome

maximum = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if is_palindrome(i*j) and i*j > maximum:
            maximum = i*j
print(maximum)
