from graham import *

start = None
goal = None
obstacles = []

try:
    with open('inputs.txt', "r") as f:
        lines = [line.strip() for line in f if line.strip()]

except FileNotFoundError:
    print("File not found!")
    exit()

i = 0
while i < len(lines):
    line = lines[i]

    match line:
        case "START":
            x, y = map(int, lines[i + 1].split())
            start = (x, y)
            i += 2

        case "GOAL":
            x, y = map(int, lines[i + 1].split())
            goal = (x, y)
            i += 2

        case "OBSTACLES":
            i += 2
            

        case "POINTS":
            num_points = int(lines[i + 1])
            polygon = []
            for j in range(num_points):
                polygon.append(tuple(map(int, lines[i + 2 + j].split())))
            obstacles.append(polygon)
            i += 2 + num_points

        case _:
            i += 1


obstacles = [graham_scan(points) for points in obstacles]