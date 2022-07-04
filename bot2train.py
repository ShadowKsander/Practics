import math


def main(z):
    if z < 3:
        return 8 * z ** 4
    if -3 <= z < 51:
        return 40 * z ** 2
    if 51 <= z < 96:
        return 22 * math.tan(z) ** 5 - 29 * math.ceil(z) ** 7
    return 10 * (22 * z ** 3) ** 4

print(main(-15))