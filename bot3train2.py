import math


def main(b, a, n, m):
    total = 0
    left = 0
    right = 0
    for k in range(1, b + 1):
        left += k ** 2 + 72 * k ** 3 - 1 - k + math.tan(k) ** 4
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            for c in range(1, a + 1):
                right += (23 * j ** 2) ** 4 + (c ** 2 + 30 * c + 38 * i ** 3 ) ** 2
    return left - right

print(main(8, 4, 6, 2))