def vp(va, vb, i, m):
    return sum([
        va[i][j] * vb[j]
        for j in range(m)
    ])


n, m = map(int, input().split())

A = []
b = []

for _ in range(n):
    A.append(list(map(int, input().split())))

for _ in range(m):
    b.append(int(input()))

for i in range(n):
    print(vp(A, b, i, m))
