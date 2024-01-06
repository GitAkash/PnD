import numpy as np
import matplotlib.pyplot as plt


def parabool(x, a, b=0, c=0):
    return a * x ** 2 + b * x + c


plt.plot(np.linspace(-10, 10, 1000), parabool(x=np.linspace(-10, 10, 1000), a=1, b=2, c=3), label="Parabool")
plt.scatter(np.linspace(-10, 10, 21), parabool(x=np.linspace(-10, 10, 21), a=1, b=2, c=3), marker="*", color='r',
            label="Gehele Getallen")
plt.xlabel("x")
plt.ylabel("y = x**2 + 2x + 3")
plt.title("Parabool met gehele getallen gemarkeerd")
plt.legend()
plt.grid()
plt.show()