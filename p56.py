# Problem 56
# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


maximum = 0
for i in range(0, 100):
    for j in range(0, 100):
        maximum = max(maximum, sum_digits(i**j))
print(maximum)