"""
A. Oversized Pancake Flipper
"""

from functools import lru_cache


def main():
    t = int(input())
    for i in range(1, t + 1):
        cakes, flipper = input().split(" ")
        print("Case #{}: {}".format(i, find_min_step(cakes, int(flipper))))


def find_min_step(cakes, flipper):
    """
    >>> find_min_step('---+-++-', 3)
    3
    >>> find_min_step('+++++', 4)
    0
    >>> find_min_step('-+-+-', 4)
    'IMPOSSIBLE'
    """

    return bidirectional_search(cakes, flipper)


def bidirectional_search(cakes, flipper):
    final = final_state(cakes)
    depth = 0

    visited_f = {}
    states_f = [cakes]

    visited_b = {}
    states_b = [final]

    while True:
        # forward
        s_f = [x for x in states_f if x not in visited_f]

        for x in s_f:
            visited_f[x] = depth
        states_f = [cake for x in s_f for cake in next_states(x, flipper)]

        # backward
        s_b = [x for x in states_b if x not in visited_b]

        for x in s_b:
            visited_b[x] = depth
        states_b = [cake for x in s_b for cake in next_states(x, flipper)]

        # test
        depth += 1

        dup = [b for f in visited_f for b in visited_b if b == f]

        if len(dup) != 0:
            return visited_f[dup[0]] + visited_b[dup[0]]
        elif len(s_f) == 0 or len(s_b) == 0:
            return 'IMPOSSIBLE'


@lru_cache(maxsize=None)
def next_states(cakes, flipper):
    """
    >>> next_states('++++', 2)
    ['--++', '+--+', '++--']
    >>> next_states('++++', 3)
    ['---+', '+---']
    >>> next_states('++++', 4)
    ['----']
    >>> next_states('-+-+', 2)
    ['+--+', '--++', '-++-']
    >>> next_states('-+-+', 3)
    ['+-++', '--+-']
    >>> next_states('-+-+', 4)
    ['+-+-']
    """

    return [flip_cakes(cakes, flipper, i) for i in range(len(cakes) - flipper + 1)]


@lru_cache(maxsize=None)
def flip_cakes(cakes, flipper, index):
    """
    >>> flip_cakes('---+-++-', 3, 0)
    '++++-++-'
    >>> flip_cakes('++++-++-', 3, 5)
    '++++---+'
    >>> flip_cakes('++++---+', 3, 4)
    '++++++++'
    """

    return cakes[:index] + ''.join(map(flip_cake, cakes[index:index + flipper])) + cakes[index + flipper:]


@lru_cache(maxsize=None)
def flip_cake(cake):
    """
    >>> flip_cake('+')
    '-'
    >>> flip_cake('-')
    '+'
    """

    return '+' if cake == '-' else '-'


@lru_cache(maxsize=None)
def final_state(cakes):
    """
    >>> final_state('---+-++-')
    '++++++++'
    >>> final_state('+++++')
    '+++++'
    >>> final_state('-+-+-')
    '+++++'
    """

    return '+' * len(cakes)


if __name__ == '__main__':
    main()
