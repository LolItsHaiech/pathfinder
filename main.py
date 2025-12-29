start = None
goal = None
obs = []

with open('input.txt', "r") as f:
    lines = [line.strip() for line in f if line.strip()]

i = 0
while i < len(lines):
    line = lines[i]

    if line == "START":
        x, y = map(int, lines[i + 1].split())
        start = (x, y)
        i += 2

    elif line == "GOAL":
        x, y = map(int, lines[i + 1].split())
        goal = (x, y)
        i += 2

    elif line == "OBSTACLES":
        i += 2

    elif line == "POINTS":
        num_points = int(lines[i + 1])
        polygon = []
        for j in range(num_points):
            x, y = map(int, lines[i + 2 + j].split())
            polygon.append([x, y])
        obs.append(polygon)
        i += 2 + num_points

    else:
        i += 1


