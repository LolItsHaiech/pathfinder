class Node:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.g = float('inf')
        self.h = 0.0
        self.f = float('inf')
        self.parent = None

    def f_compare(self, other):
        if self.f == other.f:
            return self.h < other.h
        return self.f < other.f

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    # for hashing in dict in graph
    def __hash__(self):
        return hash((self.x, self.y))
