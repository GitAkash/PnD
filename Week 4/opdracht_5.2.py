# Consider the following experiment in which we want to measure the speed of sound. In a
# cylinder, that is open on one side and contains some water, we excite a resonance by blowing
# across the opening (see figure). The frequency of the produced sound is measured. This
# procedure is repeated for different amounts of water. The acquired data is collected in the
# table. When we blow across the opening a standing wave is created that has a node (zero
# amplitude) at the water-air interface and an anti-node (maximum amplitude) just above the
# opening of the cylinder. The distance between node and anti-node is 1 / 4 λ, with λ the wavelength
# of the produced sound. The anti-node is an unknown distance d above the opening. If the
# volume of water is increased, sound with a higher pitch is produced as the distance between
# node and anti-node is reduced. The speed of sound v is related to the frequency (pitch) f and
# the wavelength λ as: v = f λ.

# Assignment: Determine the speed of sound v and the distance d using the data given. Also
# include their standard errors. Make sure you do all the checks to determine if the fit is valid.

import numpy as np
import curvefitgui as cfg

hoogteWater = np.array(
    [0.018, 0.065, 0.120, 0.162, 0.212, 0.261, 0.310, 0.357, 0.406, 0.456, 0.505]
)  # m
frequentie = np.array(
    [134.3, 145.2, 160.3, 175.7, 196.3, 222.6, 255.7, 301.3, 366.4, 468.9, 648.4]
)  # Hz

hwl = 0.001 / np.sqrt(len(hoogteWater))
fsl = 0.1 / np.sqrt(len(frequentie))

hoogteWater_sigma = np.ones(len(hoogteWater)) * hwl  # m
frequentie_sigma = fsl / frequentie**2  # Hz

print(hwl)
print(fsl)


cfg.linear_fit_gui(
    1 / frequentie,
    hoogteWater,
    xlabel="1/Frequentie in seconden",
    ylabel="hoogteWater in meter",
    xerr=frequentie_sigma,
    yerr=hoogteWater_sigma,
)
