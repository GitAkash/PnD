import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Provided data
sizes = np.array([11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 201, 211, 221, 231, 241, 251, 261, 271, 281, 291, 301, 321, 311, 331, 341, 351, 361, 381, 371, 391, 401, 411, 421, 431, 441])

average_times = np.array([0.005174612300179433, 0.015053690141648986, 0.033632937759684865, 0.04777924580062973, 0.06961400741914986, 0.08391818192059873, 0.1291383529995801, 0.1568771489194478, 0.1921782244782662, 0.24951127243984955, 0.2831853768599103, 0.37069358337903396, 0.3624744516206556, 0.46112551122059814, 0.528383178699296, 0.5939380585405161, 0.7501061540999217, 0.7632586910593091, 0.9699690358398948, 0.998147337778937, 1.277550750139635, 1.3654516730006434, 1.4308237066821312, 1.6357998296213918, 2.018334763900202, 2.047915798460017, 2.2789746682805707, 2.881258250240935, 2.902171563718875, 2.772575090501341, 3.3562828385009196, 3.5805650771391813, 4.076977913539158, 4.7126176000406845, 4.791536872359575, 5.332139620219532, 5.179810511578689, 5.498655033979739, 6.930385607580247, 6.592733936080476, 6.878666058719391, 8.09902977599966, 8.879599456959696, 8.287156092920341])


def scaling_function(x, a, b):
    return a * x ** b


params, covariance = curve_fit(scaling_function, sizes, average_times)

a, b = params

fitted_values = scaling_function(sizes, a, b)

plt.scatter(sizes, average_times, label='Original Data')
plt.plot(sizes, fitted_values, label=f'Fitted Curve: a={a:.4f}, b={b:.4f}', color='red')
plt.xlabel('Size')
plt.ylabel('Average Time (seconds)')
plt.legend()
plt.show()

print(f'Fitted Parameters: a={a:.4f}, b={b:.4f}')


def calculate_estimated_time(size, a, b):
    return a * size ** b


desired_size = 2000

estimated_time = calculate_estimated_time(desired_size, a, b)

print(
    f'Estimated time for size {desired_size}: {estimated_time:.6f} seconds, or {estimated_time / 60:.6f} minutes, or {estimated_time / 3600:.6f} hours')
