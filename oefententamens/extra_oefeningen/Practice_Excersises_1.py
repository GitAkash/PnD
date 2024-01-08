import math

import numpy as np


# Opgave 1 - Count even numbers
def counteven(arr):
    even = [i for i in arr if i % 2 == 0]
    return (len(even))


# Opgave 2 - Sin(x)
x = np.sin(np.linspace(-10, 10, 100))
y = np.sin(np.arange(-10, 10, 0.25))

# Opgave 3 - Combining Arrays
A = np.array([1, 2, 3, 4, 5])
B = np.array([2, 6, 9, 12, 13])
C = np.array([-23, 45, 12, 35, 36])
D = np.concatenate((A, B))
E = np.column_stack((A, B, C))

# Opgave 4 - Translation
english = ['one', 'two', 'three', 'four', 'five']
dutch = ['een', 'twee', 'drie', 'vier', 'vijf']
eng_dutch = []

# Opgave 5 - Elfstedentocht
tocht = [9, 12, 17, 29, 33, 40, 41, 42, 47, 54, 56, 63, 85, 86, 97]
tocht_new = [i + 1900 for i in tocht]
tocht_after45 = [i + 1900 for i in tocht if i > 45]


def tocht_tijd(arr):
    for i in range(len(arr)):
        print(f"Elfstedentocht {i} was in '{arr[i]}")


# Opgave 6 - Euler-Mascheroni constant
def euler_mascheroni(N):
    gamma = -np.log(N)
    for i in range(1, N):
        gamma += 1 / i
    return gamma


# Opgave 7 - Average Per Item
mark_1 = [7, 9, 4, 5, 7]
mark_2 = [6, 5, 5, 8, 9]
average = [(i + j) / 2 for i, j in zip(mark_1, mark_2)]

# Opgave 9 - Circle
x = np.random.uniform(-1, 1, 100)
y = np.random.uniform(-1, 1, 100)
p = np.column_stack((x, y))
c = [i for i in (p[:, 1] ** 2 + p[:, 0] ** 2) if 0.5 < i < 1.0]


# Opgave 10 - Unique Elements
def unique(list):
    unique = []
    for i in list:
        if i not in unique:
            unique.append(i)
    return unique


# Opgave 11 - Fractions & Factorial Sum
def fractions(N):
    s = 0
    for i in range(1, N):
        s += 1 / math.factorial(N)
    return s


# Opgave 12 - Doubles
def doubles(list):
    doubles = []
    for i in range(len(list)):
        for j in range(i + 1, len(list) - 1):
            if list[i] == list[j]:
                doubles.append(list[i])
    test = np.unique(doubles)
    return test
