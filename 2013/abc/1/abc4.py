"""
http://abc001.contest.atcoder.jp/tasks/abc001_4
"""

# ToDo: Fix broken script

import math

ts = [0] * 289

n = int(input())

for r in [input() for _ in range(n)]:
    s, e = r.split('-')

    sh, sm = map(int, [s[0:2], s[2:4]])
    eh, em = map(int, [e[0:2], e[2:4]])

    sm = math.floor((sm / 5)) * 5
    em = math.ceil((em / 5)) * 5

    si = (sh * 60 + sm) // 5
    ei = (eh * 60 + em) // 5

    for i in range(ei - si + 1):
        ts[si + i] += 1

rs = [i for i, v in enumerate(ts) if v >= 1]
si = ([i for i in range(1, len(rs)) if rs[i] - rs[i - 1] != 1])
sl = [rs[x:y] for x, y in zip([0] + si, si + [None])]

for r in sl:
    s = '{0:02d}{1:02d}'.format(r[0] * 5 // 60, (r[0] * 5) % 60)
    e = '{0:02d}{1:02d}'.format(r[len(r) - 1] * 5 // 60, (r[len(r) - 1] * 5) % 60)
    print('-'.join([s, e]))
