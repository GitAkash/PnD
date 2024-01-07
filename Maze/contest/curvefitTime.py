import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Provided data
sizes = np.array([11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 201,
                  211, 221, 251, 231, 241, 261, 271, 281, 301, 291, 311, 321, 331, 341, 351, 361, 371, 391, 401,
                  381, 411, 431, 421, 441, 451, 461, 471, 481, 491])

average_times = np.array([
    0.0042674128801445475, 0.016951509299397004, 0.03493421521910932, 0.048735585398972034,
    0.06733346394117688, 0.0921932171593653, 0.12595576007995987, 0.14943278192105935,
    0.18450715800077888, 0.21609713570098393, 0.31328950676048406, 0.4043550529589993,
    0.4328728554394911, 0.45135955097852276, 0.5606351408397313, 0.584122724920162,
    0.7771276016990305, 0.8984042068806594, 0.8840196401186404, 1.0493962614590417,
    1.095606057459663, 1.3622521194594446, 1.5291887701200904, 1.8595672689774074,
    1.7003234514803625, 1.974644865980954, 2.1747167437386814, 2.589669580179907,
    2.5442631536594127, 3.2709110342807253, 3.1957308226815075, 3.8543748703808522,
    3.7177497838815907, 4.459738230140065, 4.048702826920489, 4.5420850571204205,
    5.1247226408589635, 5.542953418859979, 5.407326687918976, 6.204264703819645,
    6.495395167320676, 5.693551885520574, 6.965732753319316, 6.855333488979668,
    6.902015150340449, 6.759508493160247, 7.318896990820358, 6.407392891540658,
    6.018842419618741
])

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


desired_size = 1000000

estimated_time = calculate_estimated_time(desired_size, a, b)

print(
    f'Estimated time for size {desired_size}: {estimated_time:.6f} seconds, or {estimated_time / 60:.6f} minutes, or {estimated_time / 3600:.6f} hours')
