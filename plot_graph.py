import matplotlib.pyplot as plt

def plot_graph_and_path(graph, obstacles, path):
    plt.figure(figsize=(8, 7))

    # plot obstacles
    for poly in obstacles:
        xs = [p.x for p in poly] + [poly[0].x]
        ys = [p.y for p in poly] + [poly[0].y]
        plt.plot(xs, ys, color='black', linewidth=1)

    # plot edges
    for u in graph:
        for v, w in graph[u]:
            plt.plot([u.x, v.x], [u.y, v.y], color='red', linewidth=0.5)

    # plot path
    if path is not None and len(path) > 1:
        xs = [p.x for p in path]
        ys = [p.y for p in path]
        plt.plot(xs, ys, color='green', linewidth=3, label='Path')

    # plot nodes
    for node in graph.keys():
        plt.scatter(node.x, node.y, color='blue', s=20)

    # settings
    plt.title("Graph (Red) and Path (Green)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()
