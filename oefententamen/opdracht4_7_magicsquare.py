import numpy as np

m = np.array([[2, 7, 6],
              [9, 5, 1],
              [4, 3, 8]])
# m = np.array([[1, 2], [3, 4]])
def magic_square(m):
    side_len = len(m[:])
    diagonal0_list = []
    diagonal1_list = []

    for i in range(side_len):
        row = (m[i, :])
        column = (m[:, i])

        for j in range(side_len):
            diagonal0_list.append((m[j, i]))
            diagonal1_list.append(m[j, side_len-1-i])

        return np.sum(row) == np.sum(column) == np.sum(diagonal1_list) == np.sum(diagonal0_list)

print(magic_square(m))