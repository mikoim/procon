# TODO refactoring


def char(n, h):
    tbl = ['#', '.']

    if h % 2 == 1:
        tbl = ['.', '#']

    if n % 2 == 0:
        return tbl[0]
    else:
        return tbl[1]


while True:
    h, w = map(int, input().split())

    if h == 0 and w == 0:
        break

    for i in range(h):
        print(''.join([char(n, i) for n in range(w)]))

    print()
