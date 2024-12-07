import networkx
import functools

graph = networkx.Graph()
with open("input", "r") as inf:
    for line in inf:
        s, e = line.rstrip().split(": ")
        for t in e.split(" "):
            graph.add_edge(s, t)
cuts = networkx.minimum_edge_cut(graph)
graph.remove_edges_from(cuts)

print(functools.reduce(lambda x, y: x*y, map(len, networkx.connected_components(graph))))
