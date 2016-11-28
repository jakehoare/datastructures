_author_ = 'jake'
_project_ = 'datastructures'

import graph, adaptable_priority_queue, math, numpy as np
from collections import defaultdict
from matplotlib import pyplot as plt


def heuristic(a, b):
    """
    :param a: (row, col) tuple
    :param b: (row, col) tuple
    :return: straight line distance between 2d points a and b
    """
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def search(world, start, target):
    """
    :param world: Graph
    :param start: (row, col) tuple
    :param target: (row, col) tuple
    :return: Best path from start to target as a list of (row, col) tuples, else [] if no such path.
    """
    frontier = adaptable_priority_queue.Apq_heapq()     # apq with value = point, priority = g + h
    visited = set()                                     # set of points
    g = defaultdict(lambda : float('inf'))              # best path distance from start to node
    previous = {}                                       # map node to previous node

    start_node = world.nodes[start]
    g[start_node] = 0
    previous[start_node] = None
    frontier.add_value(start_node, heuristic(start, target))

    while frontier:

        node = frontier.pop_min()
        if node.label == target:
            return get_path(previous, node)
        visited.add(node)

        nbors = set(nbor for nbor, _ in node.edges) - visited
        for nbor in nbors:
            if g[node]+1 < g[nbor]:         # path from node to nbor is better than any previous path to nbor
                g[nbor] = g[node]+1         # distance between neighbours is 1
                previous[nbor] = node
                frontier.add_value(nbor, g[nbor] + heuristic(nbor.label, target))   # add or update priority

    return []   # target not reachable


def get_path(previous, node):
    """
    :param previous: dictionary of best node from which to reach key node
    :param node: end nde of path
    :return: list of (row, col) tuples from start to node
    """
    path = []
    while node:
        path.append(node.label)
        node = previous[node]
    return path[::-1]


def diaplay(world, path):
    """
    :param world: Graph of 2d points
    :param path: list of points
    :return: None, displays 2d world overlaid with path
    """
    xs, ys = zip(*world.nodes.keys())
    grid = np.ones((max(xs) - min(xs) + 3, max(ys) - min(ys) + 3), dtype=int)   # 1 cell border around edge
    for cell in world.nodes.keys():
            grid[(cell[0] - min(xs) + 1, cell[1] - min(ys) + 1)] = 0
    for cell in path:
            grid[(cell[0] - min(xs) + 1, cell[1] - min(ys) + 1)] = 2
    plt.imshow(grid, interpolation='nearest')
    plt.show()



if __name__ == "__main__":
    world = graph.graph_from_txt("medium_maze.txt")
    path = search(world, (1, 1), (29, 44))
    diaplay(world, path)