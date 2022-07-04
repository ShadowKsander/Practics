import math


def main(y, x, z):
    a = math.atan(5 * z ** 3 + y ** 2) ** 5
    b = 78 * (x ** 2 - 24) ** 6
    c = 84 * (72 * z ** 2 - y ** 3 - z) ** 7 - 26 * x
    d = 69 * (x / 70 - (z ** 2) / 80) ** 6 - 49 * (72 + 36 * y) ** 5
    return a + b + c / d

print(main(-0.99, 0.09, 0.27))