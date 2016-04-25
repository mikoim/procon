"""
http://abc002.contest.atcoder.jp/tasks/abc002_3
"""

xa, ya, xb, yb, xc, yc = map(int, input().split())
print(abs(xa * (yb - yc) + xb * (yc - ya) + xc * (ya - yb)) / 2)