import math


def float_print(v):
    print('{:.5f}'.format(v))


a, b, C = map(float, input().split())
C = math.radians(C)

float_print(a * b * math.sin(C) / 2)
float_print(a + b + math.sqrt(math.pow(a, 2) + math.pow(b, 2) - 2 * a * b * math.cos(C)))
float_print(b * math.sin(C))
