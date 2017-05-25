a, b = map(int, input().split())

if a == b:
    op = '=='
elif a > b:
    op = '>'
else:
    op = '<'

print('a', op, 'b')
