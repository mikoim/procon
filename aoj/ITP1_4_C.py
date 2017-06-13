while True:
    f = input()
    a, op, b = f.split()

    if op == '?':
        break

    print(int(eval(f)))
