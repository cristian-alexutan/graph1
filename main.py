from graph import DirectedGraph, GraphError, read_graph_from_file, write_graph_to_file, random_graph

g = read_graph_from_file("graph.txt")
for x in g.vertices():
    ans = f"{x}: "
    for y in g.outbound(x):
        ans += f"{y} "
    print(ans)
write_graph_to_file("graph.txt", g)