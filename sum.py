# Ventu test - exercise 1
import math

def addNumbers(a: float, b: float):
    if (a < 0) or (b < 0):
        return "numbers must be positives"

    else:

        total = math.floor(a + b)

        return total

print(addNumbers(2.34, 5.7))