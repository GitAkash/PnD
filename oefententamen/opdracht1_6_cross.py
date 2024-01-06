# -*- coding: utf-8 -*-
"""
data definitions exercise 6 session 14 2023
"""
import numpy as np
# Position data in format [[rx1, ry1, rz1],[rx2, ry2, rz2], etc] units: meter
# each row is the position of a pointmass and the three columns are the x, y and z
#components of the position
r = np.array([[12985508818.8722, 144914044674.365, -6599781.81649925],
[43193952004.5904, -42554673676.9047, -7440194632.30252],
[-98167038350.0724, 36052297906.6891, 6159043110.69824],
[-242365353762.880, 52189539555.2175, 7041891974.50660],
[-769248096608.408, 252350708807.957, 16165324843.5966],
[-565951878630.631, -1385444847294.29, 46611757353.4297],
[2825476610823.50, 972932659454.854, -32974196876.2502],
[4179099711535.99, -1618518388286.26, -62976492501.0348]])

# Velocity data in format [[vx1, vy1, vz1], [vx2, vy2, vz2], etc] units: m/s
# each row is the velocity of a pointmass and the three columns are the x, y and z
#components of the velocity
v = np.array([[-30107.5452233050, 3152.57211808981, 0.239203257806707],
[24053.9197281712, 37930.4565497605, 892.593169893870],
[-13168.5532122993, -33260.0117626774, 303.938465688871],
[-4407.30732138063, -21377.0041321776, -339.782633119299],
[-4206.26381810354, -11669.7236711066, 142.508355685171],
[8313.94242990905, -3655.67965367811, -267.535432902485],
[-2240.21709526944, 6040.38165453190, 51.6243650018807],
[1903.76676204510, 5030.32721729349, -147.245293613301]])

# Mass data in format [m1, m2, etc] units: Kg
m = np.array([5.96700000000000e+24,
3.58020000000000e+23,
4.89294000000000e+24,
6.56370000000000e+23,
1.89673029000000e+27,
5.67700380000000e+26,
8.68795200000000e+25,
1.02692070000000e+26])
#
# p_list = []
# for mass in m:
#     p_list.append(mass*v)
# p = np.asarray(p_list)
#
# l = np.cross(p, r)
# final = [np.sum(row) for row in l]
# print(final)

def cross(a, b):
    c = np.array([a[1] * b[2] - a[2] * b[1],
    a[2] * b[0] - a[0] * b[2],
    a[0] * b[1] - a[1] * b[0]])
    return c

def impulsmoment(r, m, v):
    moment = np.sum([cross(ar, am * av) for ar, am, av in zip(r, m, v)], axis=0)
    return moment

moment_system = impulsmoment(r, m, v)
print(f'{moment_system} kg m2 / s')