# Problem 55
# How many Lychrel numbers are there below ten-thousand?

from helper_functions import is_palindrome

total = 0
for i in range(0, 10000):
    n = i
    n = n + int(str(n)[::-1])
    counter = 1
    while (not is_palindrome(n)) and counter <= 50:
        n = n + int(str(n)[::-1])
        counter += 1
    if counter >= 50:
        total += 1

print(total)
