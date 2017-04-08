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

    return bfs(cakes, flipper)


def bfs(cakes, flipper):
    depth = 0
    visited = {}
    states = [cakes]

    while True:
        s = [x for x in states if x not in visited]

        if len(s) == 0:
            return 'IMPOSSIBLE'
        elif final_state(cakes) in s:
            return depth
        else:
            for x in s:
                visited[x] = depth
            states = [cake for x in s for cake in next_states(x, flipper)]
            depth += 1


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
