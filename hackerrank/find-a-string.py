a = input()
b = input()

c = 0
t = 0

while True:
    a = a[c:]
    r = a.find(b)

    if r == -1:
        break
    else:
        c = r + 1

    t += 1

print(t)