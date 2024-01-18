# Opgave 1 - Insertion Sort
import math

import numpy as np


def insertionSort(array):
    for i in range(1, len(array)):
        for j in range(i - 1, -1, -1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


# Opgave 2 - Matrix Multiplication


# Opgave 3 - Prime Factorisation
def prime_factors(number):
    prime_factors = []
    i = 2
    while number / i != 1:
        if number % i == 0:
            number /= i
            prime_factors.append(i)
        else:
            i += 1
    prime_factors.append(int(number))
    return prime_factors


# Opgave 4 - Sub List Check
def find_sequence(test_list, sub_list):
    count = 0
    for i in range(len(test_list)):
        if sub_list[i % len(sub_list)] != test_list[i]:
            if count != len(sub_list):
                count = 0
            else:
                return True
        else:
            count += 1
    return False


# Opgave 5 - Geometric Mean
def geomean(n):
    if np.any(n) < 0:
        if i < 0:
            return -1
    return np.prod(n) ** (1 / len(n))


# Opgave 6 - Golden Ratio
def golden_ratio_rec(n):
    if n == 0:
        return 1
    return 1 + 1 / golden_ratio_rec(n - 1)


def golden_ratio(n):
    ratio = 1
    for i in range(n):
        ratio = 1 + 1 / ratio
    return ratio


# Opgave 7 - Average Infections

# Opgave 8 - Plotting

# Opgave 9 - Smallest Unique Numbers
def smallest(l, n):
    return np.sort(np.unique(n))[:l]

# Opgave 10 - Logistic Map
def logistic_map(r, n):
    if n == 0:
        return 0.5
    return r * logistic_map(r, n-1) * (1 - logistic_map(r, n-1))
def logistic_map_2():
    list = []
    for i in range(10):
        list.append(logistic_map(3.4, i))
    return list

# Opgave 11 - Anagrams
def anagram(word1, word2):
    return sorted(word1) == sorted(word2)

# Opgave 12 - Longest increasing
def length_longest_increasing(x):
    maxCount = 0
    count = 0
    for i in range(0, len(x)):
        if x[i-1] < x[i]:
            count += 1
            if count > maxCount:
                maxCount = count
        else:
            count = 1
    return maxCount

# Opgave 13 - Angular Momentum

# Opgave 14 - Perfect numbers
def perfect(n):
    divisor = []
    if n < 1:
        return False
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    return np.sum(divisor) == n

def firt_n_perfect():
    perfect2 = []
    for i in range(1, 10000):
        if perfect(i) == True:
            perfect2.append(i)
    print(perfect2)

# Opgave 15 - Madelung constant
    def madelung(m, n):
        alpha = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i % 2 == 1 and j % 2 == 1:
                    alpha += np.cosh(np.pi / 2 * (np.sqrt(i ** 2 + j ** 2))) ** (-2)
        alpha = alpha * 12 * np.pi
        return alpha
