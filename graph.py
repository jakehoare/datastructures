_author_ = 'jake'
_project_ = 'datastructures'

class Node:
    """
    Node for use in Graph
    """
    def __init__(self, label):
        self.label = label
        self.edges = []     # list of (Node, weight) tuples

class Graph:
    """
    Directed graph represented as adjacency list with weighted edges
    """
    def __init__(self):
        self.nodes = {}     # mapping from label to nodes


def graph_from_txt(file):
    """
    Converts a text file to a 2D Graph.  Space chars are nodes.  Edge border must consist of non-space chars.
    Node labels are [row, col) tuples.
    :param file: string
    :return: graph_2d: Graph
    """
    array = []
    with open(file) as f:
        for line in f:
            array.append([0 if c == ' ' else 1 for c in line.strip()])
    f.close()

    graph_2d = Graph()
    rows, cols = len(array), len(array[0])

    for r in range(rows):
        for c in range(cols):
            if array[r][c] == 0:
                graph_2d.nodes[(r, c)] = Node((r, c))

    for r in range(rows):
        for c in range(cols):
            if array[r][c] == 0:
                if array[r+1][c] == 0:
                    graph_2d.nodes[(r, c)].edges.append((graph_2d.nodes[(r+1, c)], 1))
                if array[r-1][c] == 0:
                    graph_2d.nodes[(r, c)].edges.append((graph_2d.nodes[(r-1, c)], 1))
                if array[r][c+1] == 0:
                    graph_2d.nodes[(r, c)].edges.append((graph_2d.nodes[(r, c+1)], 1))
                if array[r][c-1] == 0:
                    graph_2d.nodes[(r, c)].edges.append((graph_2d.nodes[(r, c-1)], 1))

    return graph_2d