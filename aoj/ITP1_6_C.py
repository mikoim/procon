rooms = [[[0 for k in range(10)] for j in range(3)] for i in range(4)]
n = int(input())

for _ in range(n):
    b, f, r, v = map(int, input().split())
    rooms[b - 1][f - 1][r - 1] += v

for b in range(4):
    for f in range(3):
        print(' ' + ' '.join(map(str, rooms[b][f])))
    if b is not 3:
        print('####################')
