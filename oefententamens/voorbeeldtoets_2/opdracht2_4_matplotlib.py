import numpy as np
import matplotlib.pyplot as plt

k = 1
w_n = 1
q = 0.25
w = np.array([-10, -5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
H = k / np.sqrt( (1-(w/w_n)**2)**2 + 4 * (q**2) * (w/w_n)**2)

x_as = w_n/w
y_as = H
z = 50-4*w

fig, ax = plt.subplots(figsize=(7,3.5))
ax.plot(x_as, y_as, z)

plt.grid()
plt.show()