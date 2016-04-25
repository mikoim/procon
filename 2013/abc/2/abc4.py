"""
http://abc002.contest.atcoder.jp/tasks/abc002_4
"""

# ToDo: Fix broken script

n, m = map(int, input().split())
fl = [v | (1 << i) for i, v in enumerate([int('0' * n, 2)] * n)]

for r in [input() for _ in range(m)]:
    def flag(x, y):
        fl[x] |= 1 << y
        fl[y] |= 1 << x
    m1, m2 = [int(x) - 1 for x in r.split()]
    flag(m1, m2)

for b in fl:
    print('{:015b}'.format(b))

print(max([sum([(b & (1 << x)) >> x for b in fl]) for x in range(n)]))
