# Opgave 1 - Bisection Method
import numpy as np


# Opgave 2 - Lucas Numbers
def first_lucas_numbers(n):
    list = []

    def Lucas(n):
        if n == 0:
            return 2
        if n == 1:
            return 1
        return Lucas(n - 1) + Lucas(n - 2)

    for i in range(n):
        list.append(Lucas(i))

    return list


first_lucas_numbers(24)


# Opgave 3 - Eleven Test
def eleven_test(account):
    numbers = [int(x) for x in str(account)][::-1]
    total = 0
    for i in range(len(numbers)):
        total += (i + 1) * numbers[i]
    if total % 11 == 0:
        return True
    return False


# Opgave 4 - Merge Sorted
def merge_sorted(list1, list2):
    i, j = 0, 0
    new_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
    new_list.extend(list1[i:])
    new_list.extend(list2[j:])
    return new_list


# Opgave 5 - Bubble Sort

# Opgave 6 - Password Check

# Opgave 7 - Approximating pi

# Opgave 8 - Another Approximation for pi

# Opgave 9 - Approximating Sine

# Opgave 10 - Bitcoin Rates

# Opgave 11 - Integral Approximation

# Opgave 12 - Magic Squares

# Opgave 13 - Neural Network

# Opgave 14 - Rock Paper Scissors
def rock_paper_scissors(player1, player2):
    player1 = str(player1)
    player2 = str(player2)

    if player1 == player2:
        return 0
    if player1 == 'rock' and player2 == 'scissors' or player1 == 'scissors' and player2 == 'paper' or player1 == 'paper' and player2 == 'rock':
        return 1
    if player2 == 'rock' and player1 == 'scissors' or player2 == 'scissors' and player1 == 'paper' or player2 == 'paper' and player1 == 'rock':
        return 2
    else:
        return -1


# Opgave 15 - Collatz Sequence

# Opgave 16 - Finding Sequences


# Opgave 17 - Caesar cipher
def caesar_encode(cipher_text, key):
    encrypted_text = ""
    for char in cipher_text:
        base = ord('A')
        encrypted_text += chr((ord(char) - base + key) % 26 + base)
    return encrypted_text


def caesar_decrypt(cipher_text, key):
    return caesar_encode(cipher_text, -key)

# Opgave 18 - Distance Table
loc = np.array([[0,0],[0,2],[2,4],[3,3],[0,4]])
route = [0, 3, 4, 2, 1]
def distance_table(loc):
    table = []
    for i in range(len(loc)):
        for j in range(len(loc)):
            table.append(np.sqrt((loc[i][0] - loc[j][0])**2 + (loc[i][1] - loc[j][1])**2))
    return np.asarray(table).reshape(len(loc), len(loc))

def dist_travel(table, route):
    distance = 0
    print(table)
    for i in range(len(route) - 1):
        step = [route[i], route[i+1]]
        distance += table[step[0], step[1]]
    return distance

# Opgave 19 - Temperature Jumps
T_data = np.array([10.2, 9.5, 11.0, 7.5, 4.3, 9.8, 10.1, 8.8])
def max_temp(tempData):
    maxTempDiff = 0
    for i in range(len(tempData)):
        for j in range(i + 1, len(tempData) - 1):
            tempDiff = tempData[j] - tempData[i]
            if tempDiff > maxTempDiff:
                maxTempDiff = tempDiff
    return maxTempDiff

# Opgave 20 - Absorbance

# Opgave 21 - Two product problem

