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

# b) Als je naar de plot kijkt, begint deze niet bij 0 maar bij 2. Als deze B er niet zou zijn,
# zou de lijn niet meer door de punten heen lopen maar daar onder.
#
# c) in curvefitgui komt de volgende info naar boven: value: 3.3241195246 g/(cm^3) & stderr: 1.1927199018e-02 g/(cm^3)
# de a is afhankelijke variable oftewel dit gaat over het de density. Aangezien V = 1/D * M + b
#
# d) in curvefitgui komt de volgende info naar boven: value: 8.5510732032e-01 g & stderr: 1.3475082074e-01 g voor de b.
# de b is de onafhankelijke variable oftewel de beker. Het gewicht van de beker blijft immers hetzelfde.
#
# e)
#
# f) S_min = 4.0228921059e-01
# from scipy.stats import sem
# print(sem(mass))
# geeft 4.8657 g
# er is dan een verschil van 4.46 gram.
#
# g= fitje
#
# h)

mylist = []
for i in mass:
    mylist.append(2)
err = np.array(mylist)

print(err)
cfg.linear_fit_gui(volume,mass, xlabel='volume', ylabel='mass', yerr=err)

