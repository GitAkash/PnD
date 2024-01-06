import numpy as np


def taxicab(p1, p2):
    return abs(p2[1] - p1[1]) + abs(p2[0] - p1[0])


p1 = np.array([-2, 1])
p2 = np.array([3, 4])

test = np.array([
    [-2, 1],
    [3, 4],
    [5, 8]])

# print(taxicab(p1, p2))


def total_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += taxicab(route[i], route[i + 1])
    return distance
