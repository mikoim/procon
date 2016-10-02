def swap(c):
    if c.isupper():
        return c.lower()
    else:
        return c.upper()


print(''.join(map(swap, input())))
