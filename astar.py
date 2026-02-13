import math
from node import Node
from p_queue import PQueue
from tree import Tree


def heuristic(node: Node, goal: Node) -> float:
    dx = node.x - goal.x
    dy = node.y - goal.y
    return math.sqrt(dx ** 2 + dy ** 2)


def reconstruct_path(node: Node):
    path = []
    current = node
    while current is not None:
        path.append(current)
        current = current.parent
    path.reverse()
    return path


def run(graph: dict[Node, list[tuple[Node, float]]], start: Node, goal: Node):
    tree = Tree()
    frontier = PQueue()

    visited: list[Node] = []
    # Zeroing all nodes
    for node in graph.keys():
        node.g = float('inf')
        node.h = 0.0
        node.f = float('inf')
        node.parent = None

    # initialize start node
    start.g = 0.0
    start.h = heuristic(start, goal)
    start.f = start.g + start.h

    # add start node to tree
    tree.insert(start)

    # add start node to frontier
    frontier.enqueue(start, -start.f)

    while not frontier.is_empty():
        current: Node = frontier.dequeue()
        if current in visited:
            continue
        visited.append(current)
        if current == goal:
            # path found and returning the path
            return reconstruct_path(current)

        # expand neighbors
        for neighbor, weight in graph[current]:
            if neighbor in visited:
                continue
            new_g = current.g + weight
            if new_g < neighbor.g:
                neighbor.g = new_g
                neighbor.h = heuristic(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current

                # add neighbor to frontier
                frontier.enqueue(neighbor, -neighbor.f)

                # add neighbor to tree
                if tree.find(neighbor) is None:
                    tree.insert(neighbor, parent_value=neighbor.parent)

    # if frontier is empty & goal is not reached, path not found
    return None
