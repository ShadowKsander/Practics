def zero(items, left, right):
    if items[0] == 'E':
        return left
    if items[0] == 'HAXE':
        return right


def four(items, left, middle, right):
    if items[4] == 1999:
        return left
    if items[4] == 2017:
        return middle
    if items[4] == 1989:
        return right


def three(items, left, right):
    if items[3] == 1989:
        return left
    if items[3] == 1973:
        return right


def two(items, left, right):
    if items[2] == 'MQL5':
        return left
    if items[2] == 'JFLEX':
        return right


def one(items, left, middle, right):
    if items[1] == 1986:
        return left
    if items[1] == 2007:
        return middle
    if items[1] == 2002:
        return right


def main(items):
    return one(
        items,
        three(
            items,
            four(items, 0, 1, zero(items, 2, 3)),
            four(items, 4, 5, zero(items, 6, 7))
        ),
        three(items, two(items, zero(items, 8, 9), 10), 11),
        12
    )
print(main(['E', 2002, 'JFLEX', 1989, 1989]))