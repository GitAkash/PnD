import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Provided data
sizes = np.array([11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 201,
                  211, 221, 251, 231, 241, 261, 271, 281, 301, 291, 311, 321, 331, 341, 351, 361, 371, 391, 401,
                  381, 411, 431, 421, 441])

average_times = np.array([0.004068738879577722, 0.016131346960319207, 0.033598722840251866, 0.06157425108001917,
                          0.09368507423976552, 0.12797882329992716, 0.20347611800098092, 0.27575803570071,
                          0.31753769992035813, 0.45826144237900734, 0.6195340289603337, 0.819935451260535,
                          1.0476799557999765, 1.3703863907996856, 1.5293684037002095, 1.9875987668795279,
                          2.3261597299799903, 2.474572047280235, 2.9677793140598805, 4.046449205879616,
                          4.118209871419822, 6.1491754977602975, 6.850549721019779, 7.495930429380096,
                          8.231311804439175, 11.651079503300133, 12.949865309660673, 14.173559569860082,
                          16.334549556699784, 17.916773188118967, 20.383475642039556, 23.46943545122005,
                          29.693634636259812, 31.83182106009961, 32.75662074537948, 39.432483114339846,
                          42.6087203002593, 52.14707089035976, 52.7164934870803, 56.247797772220075,
                          59.81806274120041, 70.29796531225992, 86.60226514534006, 89.91895798436074])


# Define the function to fit (you can change this based on the expected behavior)
def scaling_function(x, a, b):
    return a * x ** b


# Perform curve fitting
params, covariance = curve_fit(scaling_function, sizes, average_times)

# Extract the fitted parameters
a, b = params

# Generate fitted values for plotting
fitted_values = scaling_function(sizes, a, b)

# Plot the original data and the fitted curve
plt.scatter(sizes, average_times, label='Original Data')
plt.plot(sizes, fitted_values, label=f'Fitted Curve: a={a:.4f}, b={b:.4f}', color='red')
plt.xlabel('Size')
plt.ylabel('Average Time (seconds)')
plt.legend()
plt.show()

# Print the fitted parameters
print(f'Fitted Parameters: a={a:.4f}, b={b:.4f}')


# Function to calculate estimated time based on fitted parameters
def calculate_estimated_time(size, a, b):
    return a * size ** b


# Fill in your desired size for estimation
desired_size = 811

# Calculate estimated time using the fitted parameters
estimated_time = calculate_estimated_time(desired_size, a, b)

# Print the result
print(
    f'Estimated time for size {desired_size}: {estimated_time:.6f} seconds, or {estimated_time / 60:.6f} minutes, or {estimated_time / 3600:.6f} hours')
