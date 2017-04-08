"""
A. Oversized Pancake Flipper
"""


import sys

import networkx as nx
from networkx import NetworkXNoPath

sys.setrecursionlimit(0x100000)


def main():
    t = int(input())
    for i in range(1, t + 1):
        cakes, flipper = input().split(" ")
        print("Case #{}: {}".format(i, find_min_step(cakes, int(flipper))))


def memoize(f):
    cache = {}

    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return helper


def find_min_step(cakes, flipper):
    """
    >>> find_min_step('---+-++-', 3)
    3
    >>> find_min_step('+++++', 4)
    0
    >>> find_min_step('-+-+-', 4)
    'IMPOSSIBLE'
    """

    if cakes == final_state(cakes):
        return 0

    nodes = {}
    graph = nx.DiGraph()

    gen_graph_dfs(cakes, flipper, graph, nodes, 1)

    try:
        return nx.dijkstra_path_length(graph, cakes, final_state(cakes))
    except NetworkXNoPath:
        return 'IMPOSSIBLE'


def gen_graph_dfs(cakes, flipper, graph, nodes, depth):
    for nc in next_states(cakes, flipper):
        if nc in nodes and depth > nodes[nc]:
            continue

        graph.add_node(nc)
        graph.add_edge(cakes, nc)
        nodes[nc] = depth

        gen_graph_dfs(nc, flipper, graph, nodes, depth + 1)


@memoize
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


@memoize
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


@memoize
def flip_cake(cake):
    """
    >>> flip_cake('+')
    '-'
    >>> flip_cake('-')
    '+'
    """

    return '+' if cake == '-' else '-'


@memoize
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
