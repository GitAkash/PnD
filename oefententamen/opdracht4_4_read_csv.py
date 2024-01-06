import numpy as np
import matplotlib.pyplot as plt

filename = 'meting_134.csv'
t, p1, p2 = np.loadtxt(filename, delimiter=',', unpack=True)
plt.plot(t, p1, 'k', label='meting1')
plt.plot(t, p2, 'r', label='meting2')
plt.legend()
plt.xlabel('Tijd t  [s]')
plt.ylabel('Vermogen P  [W]')