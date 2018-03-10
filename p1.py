# Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_one_to_n(n):
    return n*(n+1)/2


print(3 * sum_one_to_n(333) + 5 * sum_one_to_n(199) - 15 * sum_one_to_n(66))
