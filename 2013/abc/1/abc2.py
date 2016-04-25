"""
http://abc001.contest.atcoder.jp/tasks/abc001_2
"""

import math

m = int(input()) / 1000

if m < 0.1:
    vv = 0
elif m <= 5:
    vv = m * 10
elif m <= 30:
    vv = m + 50
elif m <= 70:
    vv = math.floor(((m - 30) / 5) + 80)
else:
    vv = 89

print('{0:02d}'.format(int(vv)))
