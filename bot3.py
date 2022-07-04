import math


def main(a, m, n):
    total = 0
    for c in range(1, n + 1):
        for i in range(1, m + 1):
            for k in range(1, a + 1):
                left = math.log2(c ** 3 + i ** 2) ** 2
                right = 78 * k ** 3
                total += left + right
    return total
print(main(7, 3, 3))