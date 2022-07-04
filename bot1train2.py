import math


def main(z, x, y):
    a = 24 + (85 * x ** 3 + y ** 2 + z) ** 5
    b = (83 * y ** 2 + (x ** 3) / 10) ** 5 - 37 * math.ceil(z) ** 3
    c = math.sin(55 - x / 83 - 62 * z ** 2) / 29
    d = 63 * (62 + y ** 3) ** 3
    e = 58 * (x ** 3 + 62 * z + 80 * y ** 2) ** 6 + 9 * y ** 7
    return a / b - (c - d) / e

print (main(-0.74, -0.98, -0.84))