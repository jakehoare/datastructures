_author_ = 'jake'
_project_ = 'datastructures'

import random


def make_world(size = 20, density = 0.1):
    """
    Create a square grid of occupied and unoccupied cells
    :param size: side length
    :param density: float between 0 and 1 representing the probability that each cell is occupied
    :return: list of lists of bool
    """
    random.seed(1234)
    world = [[random.random() < density for _ in range(size)] for _ in range(size)]
    world[0][0] = world[size - 1][size - 1] = False
    return world


def world_string(world):
    """
    Converts a bool list of lists to a string with one line per row.
    Empty (False) cells are represented as 0, occupied cells are represented as 1.
    :param world: list of lists of bool
    :return: string representation of world
    """
    string = []

    for r in world:
        string.extend([str(int(x)) for x in r] + ["\n"])

    return "".join(string)
