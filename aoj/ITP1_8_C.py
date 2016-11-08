import string
import sys

table = {c: 0 for c in string.ascii_lowercase}

for raw in sys.stdin.read():
    c = raw.lower()
    if c in string.ascii_lowercase:
        table[c] += 1

for key in string.ascii_lowercase:
    print('{:s} : {:d}'.format(key, table[key]))
