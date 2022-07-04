import math


def main(y, x, z):
    a = 77 * (91 * x ** 3 - x - 25 * x ** 2) ** 3
    b = (84 * z ** 2 - 1 - 42 * y ** 3) ** 7 / 60
    c = 91 * (math.acos(81 * y ** 2 - 21 * z ** 3 - x)) ** 7
    return (math.sqrt(a-b)) - c

print(main(-0.06, 0.67, 0.13))