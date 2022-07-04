import math


def main(n, m, a, b):
    total = 1
    left = 0
    right = 0
    middle = 1
    for k in range(1, m + 1):
        for j in range(1, n + 1):
            left += k ** 2 - 48 - j / 56
    for i in range(1, n + 1):
        for c in range(1, b + 1):
            for k in range(1, a + 1):
                right += 61 * (76 * i + k ** 3 + c ** 2) ** 4
            middle += right
            right = 0
        total *= middle
        middle = 0
    return left - total

print(main(6, 8, 2, 7))