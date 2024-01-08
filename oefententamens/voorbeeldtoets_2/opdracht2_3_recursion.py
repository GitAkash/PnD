import numpy as np

xn = []

def logistic_map(r, n):
    while n != 0:
        calc = r * logistic_map(r, n - 1) * (1 - logistic_map(r, n - 1))
        xn.append(calc)
        return calc
    return 0.5

logistic_map(3.4, 10)
test = set(xn)
print(test)