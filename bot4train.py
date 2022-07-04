

def main(n):
    if n == 0:
        return 0.06
    if n == 1:
        return 0.43
    return main(n - 2) ** 3 + (main(n-1) + 40 * main(n - 2) ** 2) / 83

print(main(4))