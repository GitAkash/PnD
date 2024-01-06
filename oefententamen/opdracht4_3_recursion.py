def golden_ratio_rec(n):
    if n == 0:
        return 1
    return 1 + 1/golden_ratio_rec(n-1)

def golden_ratio2(n):
    ratio = 1
    for i in range(n):
        ratio = 1 + 1/ratio
    return ratio

print(golden_ratio2(10000))