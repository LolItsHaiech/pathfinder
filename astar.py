import math
from node import Node
from p_queue import PQueue
from tree import Tree


class AStar:
    def __init__(self, graph: dict[Node, list[tuple[Node, float]]], start: Node, goal: Node):
        self.graph = graph
        self.start = start
        self.goal = goal

        self.tree = Tree()
        self.frontier = PQueue()
        self.visited: list[Node] = []

    def heuristic(self, node: Node) -> float:
        dx = node.x - self.goal.x
        dy = node.y - self.goal.y
        return math.sqrt(dx**2 + dy**2)

    def reconstruct_path(self, node: Node):
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = current.parent
        path.reverse()
        return path

    def run(self):
        # Zeroing all nodes
        for node in self.graph.keys():
            node.g = float('inf')
            node.h = 0.0
            node.f = float('inf')
            node.parent = None

        # initialize start node
        self.start.g = 0.0
        self.start.h = self.heuristic(self.start)
        self.start.f = self.start.g + self.start.h

        # add start node to tree
        self.tree.insert(self.start)

        # add start node to frontier
        self.frontier.enqueue(self.start, -self.start.f)

        while not self.frontier.is_empty():
            current: Node = self.frontier.dequeue()
            if current in self.visited:
                continue
            self.visited.append(current)
            if current == self.goal:
                # path found and returning the path
                return self.reconstruct_path(current)

            # expand neighbors
            for neighbor, weight in self.graph[current]:
                if neighbor in self.visited:
                    continue
                new_g = current.g + weight
                if new_g < neighbor.g:
                    neighbor.g = new_g
                    neighbor.h = self.heuristic(neighbor)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current

                    # add neighbor to frontier
                    self.frontier.enqueue(neighbor, -neighbor.f)

                    # add neighbor to tree
                    if self.tree.find(neighbor) is None:
                        self.tree.insert(neighbor, parent_value=neighbor.parent)

        # if frontier is empty & goal is not reached, path not found
        return None
