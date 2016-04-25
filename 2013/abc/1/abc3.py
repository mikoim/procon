"""
http://abc001.contest.atcoder.jp/tasks/abc001_3
"""

import math

l = input().split()
d = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']
deg = int(l[0])

dire = d[int(math.floor(deg * 1000 / 225000 + 0.5))]
dis = math.floor(int(l[1]) * 100 / 600 + 0.5)

if dis <= 2:
    dire = 'C'
    w = 0
elif dis <= 15:
    w = 1
elif dis <= 33:
    w = 2
elif dis <= 54:
    w = 3
elif dis <= 79:
    w = 4
elif dis <= 107:
    w = 5
elif dis <= 138:
    w = 6
elif dis <= 171:
    w = 7
elif dis <= 207:
    w = 8
elif dis <= 244:
    w = 9
elif dis <= 284:
    w = 10
elif dis <= 326:
    w = 11
else:
    w = 12

print(dire, w)
