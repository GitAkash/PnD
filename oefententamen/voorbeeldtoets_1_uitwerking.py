# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 11:08:13 2023

@author: KangerJS

Description:
    ....
"""

import numpy as np
import matplotlib.pyplot as plt

#==================================================
# opdracht 1
# A2, B3, C4, D5, E1


#==================================================
# opdacht 2a
rng = np.random.default_rng()
x = rng.uniform(-1, 1, size=100)
y = rng.uniform(-1, 1, size=100)

# opdracht 2b
p = np.column_stack((x,y))

# opdracht 2c
s = np.sqrt(x**2 + y**2)
cirkel = p[(0.5<s)&(s<1),:]


#==================================================
# opdracht 3a
positive_integers = [i for i in range(1, 11)]

# opdracht 3b
positive_integers_div_3 = [i*3 for i in range(1, 11)]

# opdracht 3c
filenames = ['jan21_meting1.csv', 'jan23_meting1.csv', 'test1.csv', 'jan23_meting2.dat', 'feb23_meting4.csv', 'test4.csv', 'jan23_meting.dat', 'meting3.csv']
selected_files = [filename for filename in filenames if filename.startswith('jan23')]
# or
selected_files = [filename for filename in filenames if filename[0:5] == 'jan23']


#==================================================
# opdracht 4
filename = 'minmaxtemperatuur.csv'
mintemp, maxtemp = np.loadtxt(filename, delimiter=',', unpack=True)

day = [i+1 for i in range(len(mintemp))]
plt.plot(day, mintemp, 'b', label='minimum temperature')
plt.plot(day, maxtemp, 'r', label='maximum temperature')
plt.legend()
plt.xlabel('Dag')
plt.ylabel('Min/Max temperatuur / deg.Celsius')


#==================================================
# opdracht 5
filename = 'minmaxtemperatuur.csv'
mintemp, maxtemp = np.loadtxt(filename, delimiter=',', unpack=True)

MIN_PERIOD_LENGTH = 5  # days
MIN_TEMPERATURE = 25  # degree celsius

current_period_in_days = 0

for aday, temperature in enumerate(maxtemp, start=1):
    
    if temperature >= MIN_TEMPERATURE:
        current_period_in_days += 1

    else:
        
        if current_period_in_days >= MIN_PERIOD_LENGTH:
            lastday = aday - 1
            firstday = lastday - current_period_in_days + 1
            print(f'from day {firstday} to day {lastday}; duration:{current_period_in_days}')
            current_period_in_days = 0
        
        else:
            current_period_in_days = 0


#==================================================
# opdracht 6
# Position matrix in format [x1, y1, z1; x2, y2, z2; etc] units: meter
r = np.array([[12985508818.8722,   144914044674.365,   -6599781.81649925],
              [43193952004.5904,   -42554673676.9047,  -7440194632.30252],
              [-98167038350.0724,  36052297906.6891,   6159043110.69824],
              [-242365353762.880,  52189539555.2175,   7041891974.50660],
              [-769248096608.408,  252350708807.957,   16165324843.5966],
              [-565951878630.631,  -1385444847294.29,  46611757353.4297],
              [2825476610823.50,   972932659454.854,   -32974196876.2502],
              [4179099711535.99,   -1618518388286.26,  -62976492501.0348]])

# Velocity matrix in format [x1, y1, z1; x2, y2, z2; etc] units: m/s
v = np.array([[-30107.5452233050,  3152.57211808981,   0.239203257806707],
              [24053.9197281712,   37930.4565497605,   892.593169893870],
              [-13168.5532122993,  -33260.0117626774,  303.938465688871],
              [-4407.30732138063,  -21377.0041321776,  -339.782633119299],
              [-4206.26381810354,  -11669.7236711066,  142.508355685171],
              [8313.94242990905,   -3655.67965367811,  -267.535432902485],
              [-2240.21709526944,  6040.38165453190,   51.6243650018807],
              [1903.76676204510,   5030.32721729349,   -147.245293613301]])

# Mass array in format [m1; m2; etc] units: Kg
m = np.array([5.96700000000000e+24,
              3.58020000000000e+23,
              4.89294000000000e+24,
              6.56370000000000e+23,
              1.89673029000000e+27,
              5.67700380000000e+26,
              8.68795200000000e+25,
              1.02692070000000e+26])

def cross(a, b):
    '''
    computes the cross product of two vectors a and b of 3 elements each
    Parameters
    ----------
    a : numpy array of size (3,)
    b : numpy array of size (3,)
        
    Returns
    -------
    c : numpy array of size (3,)
        cross product of a and b.

    '''
    c = np.array([a[1] * b[2] - a[2] * b[1], 
                  a[2] * b[0] - a[0] * b[2], 
                  a[0] * b[1] - a[1] * b[0]])
    return c

def impulsmoment(r, m, v):
    '''
    computes the impulsmoment of a mass m at position r and velocity v 

    Parameters
    ----------
    r : numpy array of size(3,)
        position of the mass in m.
    m : float
        mass in kg.
    v : numpy array of size (3,)
        velocity of the mass in m/s

    Returns
    -------
    moment : numpy array of size (3,)
        impuls moment of the mass in kg m2 / s

    '''
    moment = np.sum([cross(ar, am * av) for ar, am, av in zip(r, m, v)], axis=0)
    return moment    
    
moment_system = impulsmoment(r, m, v)
print(f'{moment_system} kg m2 / s')


#==================================================
# opdracht 7
def bubblesort(x):
    '''
    sorts the array x from low to high using the bubblesort algoritm

    Parameters
    ----------
    x : list
        the list that gets sorted.

    Returns
    -------
    x_sorted : list
        contains the elements of x but now sorted from low to high.

    '''
    x_sorted = x.copy()  # make a copy so the original list so x is not modified

    # keep doing a pass through the list until no elements were swapped
    while True:
        has_swapped = False
        # perform a single pass through the list
        for i in range(len(x_sorted)-1):
            
            # swapp the elements in place if they are not in proper order
            if x_sorted[i] > x_sorted[i+1]:
                
                x_sorted[i+1], x_sorted[i] = x_sorted[i], x_sorted[i+1]
                has_swapped = True
        # if the current pass did not swap any element, the list is sorted
        if not has_swapped:
            break
    
    return x_sorted

# testing
x = [45, 2, -3, 67, 123, -5, 0]
x_sorted = bubblesort(x)
print(x_sorted)