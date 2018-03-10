# Problem 53
# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

from helper_functions import binomial_coefficient

total = 0

for i in range(0, 101):
    for j in range(0, i):
        if binomial_coefficient(i,j) > 1000000:
            total += 1
print(total)
