"""
http://abc003.contest.atcoder.jp/tasks/abc003_1
"""

n = int(input())
pay = 0

for i in range(1, n + 1):
    pay += 10000 * i / n

print(int(pay))
