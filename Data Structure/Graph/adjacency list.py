graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print("Adjacency List:")
for node, neighbors in graph.items():
    print(node, ":", neighbors)
