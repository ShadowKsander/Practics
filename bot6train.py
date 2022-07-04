

def zero(items, left, middle, right):
    if items[0] == 2001:
        return left
    if items[0] == 1982:
        return middle
    if items[0] == 2008:
        return right


def two(items, left, right):
    if items[2] == 1977:
        return left
    if items[2] == 2000:
        return right


def three(items, left, middle, right):
    if items[3] == 1967:
        return left
    if items[3] == 2009:
        return middle
    if items[3] == 1995:
        return right


def one(items, left, middle, right):
    if items[1] == 'OZ':
        return left
    if items[1] == 'ATS':
        return middle
    if items[1] == 'XPROC':
        return right


def main(items):
    return zero(
        items,
        three(
            items,
            one(items, 0, 1, 2),
            3,
            one(items, 4, 5, 6)),
        two(items, 7, 8),
        9)

print(main([1982, 'XPROC', 2000, 2009]))