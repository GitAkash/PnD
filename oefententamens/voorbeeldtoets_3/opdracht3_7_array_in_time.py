import numpy as np

btc_euro = np.array([102, 95, 110, 75, 43, 98, 101, 88])


def optimize_profit(btc_euro):
    max_profit = 0
    for i in range(len(btc_euro)):
        for j in range(i + 1, len(btc_euro) - 1):
            profit = btc_euro[j] - btc_euro[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit


print(optimize_profit(btc_euro))
