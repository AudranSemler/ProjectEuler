# Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def diff_sum(n):
    return int(((n*(n+1)/2)**2)-n*(n+1)*(2*n+1)/6)


print(diff_sum(100))
