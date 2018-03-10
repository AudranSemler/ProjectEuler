# Problem 2
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.


def answer():
    n0 = 1
    n1 = 1
    total = 0
    while n0 < 4000000:
        n2 = n0+n1
        # Every third term is even
        total += n2
        n0 = n2 + n1
        n1 = n0 + n2
    return total


print answer()
