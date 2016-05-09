import re

regex = '(7|8|9)\d{9,9}'

n = int(input())

for i in range(n):
    number = input()
    if len(number) is not 10 or re.match(regex, number) is None:
        print('NO')
    else:
        print('YES')