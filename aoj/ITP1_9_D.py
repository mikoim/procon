text = input()
q = int(input())

for _ in range(q):
    ops = input().split()

    if len(ops) == 3:
        op, a, b = ops
    else:
        op, a, b, p = ops

    a = int(a)
    b = int(b)

    if op == 'print':
        print(text[a:b + 1])
    elif op == 'reverse':
        text = text[:a] + ''.join(reversed(text[a:b + 1])) + text[b + 1:]
    else:
        text = text[:a] + p + text[b + 1:]
