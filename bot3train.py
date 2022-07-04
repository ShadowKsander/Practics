import math


def main(a, b, m, y):
    total = 0
    for j in range(1, m + 1):
        for i in range(1, b + 1):
            for c in range(1, a + 1):
                total += 26 * y ** 2 - 2 * j ** 3 - c - i ** 7
    return total

print(main(8, 3, 7, 0.31))