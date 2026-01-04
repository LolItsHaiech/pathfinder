import math

def _srt_key(p, p1):
    dy = p[1] - p1[1]
    dx = p[0] - p1[0]
    angle = math.atan2(dy, dx)
    if angle < 0:
        angle += 2 * math.pi
    return angle


def orientation(a, b, c):
    return a[0]*(b[1] - c[1]) + b[0]*(c[1] - a[1]) + c[0]*(a[1] - b[1])  # simplified AB x AC


def graham_scan(points: list[tuple]):
    p1 = min(points, key=lambda p: p[1])
    points.remove(p1)
    srt = sorted(points, key=lambda p: _srt_key(p, p1), reverse=True)  # todo can be optimized using cross

    stack = [p1, srt[0]]

    for i in range(1, len(srt)):
        while len(stack) >= 2 and orientation(stack[-2], stack[-1], srt[i]) >= 0:
            stack.pop()
        stack.append(srt[i])
    return stack