def main(n):
    if n == 0:
        return -0.24
    if n == 1:
        return -0.65
    return main(n - 2) ** 3 + main(n - 1) ** 2 / 48 + 0.2
print(main(5))
