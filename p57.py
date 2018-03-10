# Problem 57
# In the first one-thousand expansions of sqrt(2), how many fractions contain
# a numerator with more digits than denominator?

first = 3
second = 2
total = 0
for i in range(0, 1000):
    buffer = second
    second = first + second
    first = second + buffer

    if len(str(first)) > len(str(second)):
        total += 1
print(total)
