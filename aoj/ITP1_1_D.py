t = int(input())

h = t // 3600
t -= h * 3600

m = t // 60
t -= m * 60

s = t

print(':'.join(map(str, [h, m, s])))
