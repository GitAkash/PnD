# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:01:02 2022

@author: KangerJS
"""
"""
Uitwerkingen van sessie 14 dd 25 januari 2022
Disclaimer: gegeven oplossingen zijn slechts één van de vele
mogelijke implementaties. 
"""

import numpy as np
import matplotlib.pyplot as plt


# opdracht 1
# =========================================================#
x = np.linspace(-50, 50, 51)
y = x**2
z = np.column_stack((x,y))


# opdracht 2
# =========================================================#
z = np.array([[1, 7, 3, 9, 5], [6, 3, 8, 4, 10]])

# 2a
w = z[:,2:4]

# 2b
q = z[z>5]


# opdracht 3
# =========================================================#

# 3a
def golden_ratio_rec(N):
    """
    returns an approximation of the golden ratio according to 
    the recursive relation:
        f(0) = 1
        f(N) = 1 + 1/f(N-1)
    """
    if N == 0:
        return 1
    
    return 1 + 1 / (golden_ratio_rec(N-1))

# 3b
def golden_ratio(N):
    """
    returns an approximation of the golden ratio according to 
    the recursive relation:
        f(0) = 1
        f(N) = 1 + 1/f(N-1)
    """
    f = 1
    
    for ii in range(N):
        f = 1 + 1 / f
    
    return f    

# example of use    
print(golden_ratio_rec(20))    


# opdracht 4
# =========================================================#
# a
filename = 'meting_134.csv'
t, p1, p2 = np.loadtxt(filename, delimiter=',', unpack=True)
# b
plt.plot(t, p1, 'k', label='meting1')
plt.plot(t, p2, 'r', label='meting2')
# c
plt.legend()
# d
plt.xlabel('Tijd t  [s]')
plt.ylabel('Vermogen P  [W]')



# opdracht 5
# =========================================================#
def find_sequence(test_list, sub_list):
    """
    determines is sub_list is part of tes_list
    return True if this is the case, otherwise False
    """
    lt = len(test_list)
    ls = len(sub_list)
    
    # check for all slices of test_list of the same length as sub_list
    for ii in range(0, lt - ls + 1):
        slice_test_list = test_list[ii:ii + ls]
        
        if slice_test_list == sub_list:
            return True
    
    return False

# example of use
test_list = [5, 6, 3, 8, 2, 1, 7, 1]
sub_list = [8, 2, 1]
print(find_sequence(test_list, sub_list))


# opdracht 6
# =========================================================#
def anagram(w1, w2):
    """
    return True is w1 (string) and w2 (string) are anagrams
    """
    # convert to list and make case-insensitive
    w1 = list(w1.lower())
    w2 = list(w2.lower())
    
    # sort the list
    w1.sort()
    w2.sort()
    
    # if the sorted lists are the same it is an anagram
    is_anagram = w1 == w2
    
    return is_anagram

# example of use
w1 = 'O Draconian Devil'
w2 = 'Leonardo da Vinci'
print(anagram(w1, w2))    


# opdracht 7
# =========================================================#
def magic_square(m):
    """
    determines if m (2D NxN numpy array) is a so-called magic square
    returns True is this is the case, otherwise False
    """
    N = len(m)  # lengte van vierkant
    check_som = sum(m[0]) # alle te controleren rijen,kolommen en diag moeten dit als som hebben

    # check if all numbers are present in square
    for i in range(1, N**2 + 1):
        if i not in m:
            return False
    
    # check sums
    for i in range(N):
        # check row
        if sum(m[i,:]) != check_som:
            return False     
        # check column    
        if sum(m[:,i]) != check_som:
            return False     
    
    # check diagonals
    if sum([m[i,i] for i in range(N)]) != check_som:
        return False
    
    if sum([m[i,-i-1] for i in range(N)]) != check_som:
         return False

    return True

# example of use
m = np.array([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
print(magic_square(m))
