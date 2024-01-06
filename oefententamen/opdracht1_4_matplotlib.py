import numpy as np
import matplotlib.pyplot as plt

filename = 'minmaxtemperatuur.csv'
mintemp, maxtemp = np.loadtxt(filename, delimiter=',', unpack=True)

day = [i+1 for i in range(len(mintemp))]
plt.plot(day, mintemp, 'b', label='minimum temperature')
plt.plot(day, maxtemp, 'r', label='maximum temperature')
plt.legend()
plt.xlabel('Dag')
plt.ylabel('Min/Max temperatuur / deg.Celsius')