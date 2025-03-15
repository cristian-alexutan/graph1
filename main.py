from graph import DirectedGraph, GraphError, read_graph_from_file, write_graph_to_file

def main():
    g = DirectedGraph()
    read_graph_from_file("graph.txt", g)
    for i in range(g.vertice_count()):
        print(i, g.out_degree(i))
    write_graph_to_file("graph.txt", g)

if __name__ == "__main__":
    main()