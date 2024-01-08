import numpy as np


def madelung(m, n):
    alpha = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i % 2 == 1 and j % 2 == 1:
                alpha += np.cosh(np.pi / 2 * (np.sqrt(i ** 2 + j ** 2))) ** (-2)
    alpha = alpha * 12 * np.pi
    return alpha

print(madelung(13, 13))