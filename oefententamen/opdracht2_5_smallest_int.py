import numpy as np
z = [4, 2, 9, 678, 45, -45, -23, 34, 34, 0, -1, -1]
def smallest(z, n):
    for i in range(len(z)):
        for j in range(len(z) - 1):
            if z[j] > z[i]:
                z[j], z[i] = z[i], z[j]
    return(np.unique(z))[:n]


print(smallest(z, 4))