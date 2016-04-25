"""
http://abc003.contest.atcoder.jp/tasks/abc003_3
"""

n, k = map(int, input().split())
rl = sorted(map(int, input().split()))
c = 0

for r in rl[-k:]:
    c = (c + r) / 2

print(c)
