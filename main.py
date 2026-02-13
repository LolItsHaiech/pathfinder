from graham import *
from node import Node
from plot_graph import plot_graph_and_path
from visibility_graph import build_graph
from astar import AStar

start: Node
goal: Node
obstacles: list[list[Node]] = []

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
            start = Node(x, y)
            i += 2

        case "GOAL":
            x, y = map(int, lines[i + 1].split())
            goal = Node(x, y)
            i += 2

        case "OBSTACLES":
            i += 2

        case "POINTS":
            num_points = int(lines[i + 1])
            polygon: list[Node] = []
            for j in range(num_points):
                x, y = map(int, lines[i + 2 + j].split())
                polygon.append(Node(x, y))
            obstacles.append(polygon)
            i += 2 + num_points

        case _:
            i += 1

obstacles = [graham_scan(polygon) for polygon in obstacles]

graph = build_graph(start, goal, obstacles) 
astar = AStar(graph, start, goal) 
path = astar.run() 
if path is None: 
    print("No path found") 
else: 
    print("Path length:", len(path)) 
    for p in path: 
        print(p.x, p.y)

plot_graph_and_path(graph, obstacles, path)
