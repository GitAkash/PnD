import numpy as np

sample = np.loadtxt('sample.csv', delimiter=',', skiprows=1, unpack=True)
blanco = np.loadtxt('blanco.csv', delimiter=',')
absorbance = -np.log10(sample/blanco)

np.savetxt('absorbance.csv', absorbance, delimiter=',')