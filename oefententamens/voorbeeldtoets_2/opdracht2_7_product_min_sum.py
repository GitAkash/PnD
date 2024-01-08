import numpy as np
def two_product_problem(w, product):
    sums = [np.inf, np.inf]
    for i in w:
        for j in w:
            if i * j == product:
                if i + j < np.sum(sums):
                    sums = [i,j]

    if sums == [np.inf, np.inf]:
        return False
    else:
        return sums

print(two_product_problem([1,2,3,4,5,6], 20))