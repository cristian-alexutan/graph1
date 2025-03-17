from graph import DirectedGraph, GraphError, read_graph_from_file, write_graph_to_file

g = DirectedGraph()
read_graph_from_file("graph.txt", g)
