"""
http://abc006.contest.atcoder.jp/tasks/abc006_2
"""

a = [0] * 1000000
a[0] = 0
a[1] = 0
a[2] = 1

n = int(input())

for i in range(3, n):
    a[i] = a[i - 1] + a[i - 2] + a[i - 3]
    a[i] %= 10007

print(a[n - 1])
