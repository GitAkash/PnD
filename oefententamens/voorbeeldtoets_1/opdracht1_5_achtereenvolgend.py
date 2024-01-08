import numpy as np

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
