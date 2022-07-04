import math


def main(z):
    if z < 175:
        return (z ** 3 + 24 * z ** 2 + 22 * z) ** 5 - z ** 2 - 54 * z ** 2
    if 175 <= z < 272:
        return 50 * z ** 7
    if 272 <= z < 290:
        return (17 * z ** 2 - z) ** 6 - math.exp(z) - z ** 2
    return (math.ceil(z) ** 5) / 7 - 25

print(main(211))