#include <iostream>
#include "DirectedGraph.h"
#include "test_graph.h"

void print_menu() {
    std::cout << "1 - select graph\n";
    std::cout << "2 - get number of vertices\n";
    std::cout << "3 - parse vertices\n";
    std::cout << "4 - check if edge exists\n";
    std::cout << "5 - get in degree / out degree of vertex\n";
    std::cout << "6 - parse outbound edges of vertex\n";
    std::cout << "7 - parse inbound edges of vertex\n";
    std::cout << "8 - get cost of edge\n";
    std::cout << "9 - modify cost of edge\n";
    std::cout << "10 - add vertex\n";
    std::cout << "11 - remove vertex\n";
    std::cout << "12 - add edge\n";
    std::cout << "13 - remove edge\n";
    std::cout << "14 - create copy of graph\n";
    std::cout << "15 - read graph from file\n";
    std::cout << "16 - write graph to file\n";
    std::cout << "17 - create random graph\n";
    std::cout << "0 - exit\n";
    std::cout << "=========================================\n";
}

int switch_graph(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    std::cout << "current graph: " << graphs[index].first << "\n";
    std::cout << "current graphs:\n";
    for (int i = 0; i < graphs.size(); ++i) {
        std::cout << i << " - " << graphs[i].first << "\n";
    }
    std::cout << "enter index of desired graph";
    std::cin >> index;
    if (index < 0 || index >= graphs.size()) {
        std::cout << "Invalid index\n";
        return -1;
    }
    return index;
}

void get_number_of_vertices(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    std::cout << "number of vertices: " << graphs[index].second.vertex_count() << "\n";
}

void parse_vertices(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    std::cout << "vertices: ";
    for (auto it = graphs[index].second.vertices_begin(); it != graphs[index].second.vertices_end(); ++it)
        std::cout << *it << "\n";
    std::cout << "\n";
}

void run_ui() {
    std::vector<std::pair<std::string, DirectedGraph>> graphs;
    std::pair<std::string, DirectedGraph> graph {"graph1", DirectedGraph()};
    graphs.emplace_back(graph);
    int index = 0;
    while(true) {
        print_menu();
        int opt; std::cout << " >>> "; std::cin >> opt;
        switch(opt) {
            case 0:
                return;
            case 1: {
                int temp = switch_graph(graphs, index);
                if(temp != -1) index = temp;
            }
            case 2: {
                get_number_of_vertices(graphs, index);
            }
        }
    }
}

int main() {
    //test_graph();
    DirectedGraph g(5);
    g.remove_vertex(4);
    g.remove_vertex(3);
    g.add_edge(1, 2, 5);
    write_graph_to_file(g, "test.txt");
    system("pause");
    return 0;
}
