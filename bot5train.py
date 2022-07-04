import math


def main(y, x, z):
    n = len(y)
    y.insert(0, 0)
    x.insert(0, 0)
    z.insert(0, 0)
    total = 0
    for i in range(1, n + 1):
        total += 36 * (99 * y[i] - x[i] ** 3 - z[n + 1 - math.ceil(i / 4)] ** 2) ** 3
    return 44 * total

print(main([-0.84, -0.91, -0.9, 0.65, 0.96, -0.99, -0.03, -0.03],
[0.83, 0.82, 0.77, 0.45, 0.13, 0.72, 0.08, -0.15],
[0.88, 0.54, -0.58, -0.32, 0.9, -0.92, 0.06, -0.86]))