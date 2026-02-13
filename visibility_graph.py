import math

def orient(a, b, c):
    v = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)
    if v == 0:
        return 0
    if v > 0:
        return 1
    else:
        return 2


def proper_int(p1, q1, p2, q2):
    result = orient(p1, q1, p2) != orient(p1, q1, q2) and orient(p2, q2, p1) != orient(p2, q2, q1)
    return result


def overlap(p1, q1, p2, q2):
    if orient(p1, q1, p2) != 0:
        return False

    x_overlap = max(min(p1.x, q1.x), min(p2.x, q2.x)) < \
                min(max(p1.x, q1.x), max(p2.x, q2.x))
    y_overlap = max(min(p1.y, q1.y), min(p2.y, q2.y)) < \
                min(max(p1.y, q1.y), max(p2.y, q2.y))

    return x_overlap and y_overlap


def can_see(u, v, obstacles):
    for poly in obstacles:
        for i in range(len(poly)):
            a = poly[i]
            b = poly[(i + 1) % len(poly)]

            if u == a or u == b or v == a or v == b:
                continue

            if proper_int(u, v, a, b):
                return False

            if overlap(u, v, a, b):
                return False

    return True


def build_graph(start, goal, obstacles):
    nodes = []
    nodes.append(start)
    nodes.append(goal)

    for poly in obstacles:
        for p in poly:
            nodes.append(p)

    graph = {}
    for n in nodes:
        graph[n] = []

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u = nodes[i]
            v = nodes[j]

            if can_see(u, v, obstacles):
                d = math.hypot(u.x - v.x, u.y - v.y)
                graph[u].append((v, d))
                graph[v].append((u, d))

    return graph
