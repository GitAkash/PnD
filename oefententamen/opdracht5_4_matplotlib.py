import numpy as np
import matplotlib.pyplot as plt


def y(w_n, g):
    poop = w_n * np.sqrt(1 - g ** 2)
    return 1 - np.e ** (-g * w_n) * (np.cos(poop) + (g / (np.sqrt(1 - g ** 2))) * np.sin(poop))


w_n = np.linspace(0, 20, 100)
plt.plot(y(w_n, 0.2), color='k', linestyle='-', label='g = 0.2')
plt.plot(y(w_n, 0.7), color='k', linestyle='--', label='g = 0.7')
plt.plot(y(w_n, 0.9), color='k', linestyle='dotted', label='g = 0.9')
plt.xlim(0.0, 100.0)
plt.ylim(0.0, 2.0)
plt.legend()
plt.ylabel("y(t)")
plt.xlabel("w_n*t")
plt.grid()
plt.show()
