r, c = map(int, input().split())
last = [0] * (c + 1)

for _ in range(r):
    row = list(map(int, input().split()))
    row += [sum(row)]

    print(' '.join(map(str, row)))

    for x in range(c + 1):
        last[x] += row[x]

print(' '.join(map(str, last)))
