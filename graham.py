import math
from node import Node

def _srt_key(p: Node, p1: Node):
    dy = p.y - p1.y
    dx = p.x - p1.x
    angle = math.atan2(dy, dx)
    if angle < 0.0:
        angle += 2 * math.pi
    return angle


def orientation(a: Node, b: Node, c: Node):
    return a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y)  # simplified AB x AC


def graham_scan(points: list[Node]):
    p1: Node = min(points, key=lambda p: p.y)
    points.remove(p1)
    srt: list[Node] = sorted(points, key=lambda p: _srt_key(p, p1), reverse=True)  # todo can be optimized using cross

    stack: list[Node] = [p1, srt[0]]

    for i in range(1, len(srt)):
        while len(stack) >= 2 and orientation(stack[-2], stack[-1], srt[i]) >= 0:
            stack.pop()
        stack.append(srt[i])
    return stack