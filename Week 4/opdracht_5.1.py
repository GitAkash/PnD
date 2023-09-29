import numpy as np
import curvefitgui as cfg
from scipy.stats import sem

volume = np.array(
    [2.73, 3.92, 5.06, 6.65, 7.98, 9.43, 11.07, 12.25, 13.59, 15.1, 16.56, 18.08]
)  # cm3
mass = np.array(
    [9.7, 14.1, 17.7, 23.2, 27.3, 32.2, 37.4, 41.4, 46.2, 51.0, 56.2, 60.8]
)  # g

print(sem(mass))

mylist = []
for i in mass:
    mylist.append(2)
err = np.array(mylist)

print(err)
cfg.linear_fit_gui(volume,mass, xlabel='volume', ylabel='mass', yerr=err)

