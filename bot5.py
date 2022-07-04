import math


def main(y, x, z):
    n = len(y)
    y.insert(0, 0)
    x.insert(0, 0)
    z.insert(0, 0)
    total = 0
    for i in range(1, n + 1):
        left = 2 * y[math.ceil(i / 2)]
        middle = 17 * x[n + 1 - math.ceil(i / 4)] ** 2
        right = 56 * z[math.ceil(i / 2)] ** 3
        total += 88 * (left + middle + right) ** 6
    return 69 * total
print(main([-0.12, 0.0],[-0.32, -0.29],[-0.37, -0.46]))