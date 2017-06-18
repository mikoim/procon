import math

n = int(input())
xs = list(map(float, input().split()))
ys = list(map(float, input().split()))


def mink(p):
    return math.pow(sum([
        math.pow(math.fabs(xs[i] - ys[i]), p)
        for i in range(n)
    ]), 1 / p)


def mink_inf():
    return max([math.fabs(xs[i] - ys[i]) for i in range(n)])


def float_print(v):
    print('{:.5f}'.format(v))


float_print(mink(1))
float_print(mink(2))
float_print(mink(3))
float_print(mink_inf())
