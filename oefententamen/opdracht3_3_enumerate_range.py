import numpy as np

k = [i**2 for i in range (2, 101, 2)]

def iterator(k):
    for i in range(len(k)):
        print(f"kwadraat van {int(np.sqrt(k[i]))} is {k[i]}")

def enumerator(k):
    for i,j in enumerate(k):
        print(f"kwadraat van {int(np.sqrt(k[i]))} is {k[i]}")

enumerator(k)