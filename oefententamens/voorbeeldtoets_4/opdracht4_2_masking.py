import numpy as np

z = np.array([[1, 7, 3, 9, 5],
              [6, 3, 8, 4, 10]])


w = z[:, 2:4]
q_mask = [i > 5 for i in z]
q = z[q_mask]
# IS BETTER TO DO THIS VVV
q = z[z>5]
