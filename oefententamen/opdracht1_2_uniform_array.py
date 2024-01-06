import numpy as np

x = np.vstack((np.random.uniform(-1, 1, 100)))
y = np.vstack((np.random.uniform(-1, 1, 100)))
p = np.hstack((x,y))
cirkel_list = []
for row in p:
    distance = np.sqrt(row[0]**2 + row[1]**2)
    if 0.5 <= distance <= 1:
        cirkel_list.append(distance)

cirkel = np.vstack(np.asarray((cirkel_list)))
print(cirkel)
