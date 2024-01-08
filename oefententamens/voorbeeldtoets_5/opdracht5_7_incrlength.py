x = [23, 2, 3, 4, 88, -1, 2, 3]
def lengthlongestincreasing(x):
    count = 0
    countMax = 0
    for i in range(len(x) - 1):
        if x[i] < x[i + 1]:
            count += 1
            if count > countMax:
                countMax = count
        else:
            count = 0
    return countMax
