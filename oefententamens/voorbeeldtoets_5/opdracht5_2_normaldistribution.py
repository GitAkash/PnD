import numpy as np

x = np.random.normal(0, 1, size=(100, 200))
y = [np.sum(i) for i in x]
y1 = y[:50]
y2 = y[50:]