#include <iostream>
#include "DirectedGraph.h"
#include "test_graph.h"
#include "stdexcept"

void print_menu() {
    std::cout << "\n";
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
    std::cout << "enter index of desired graph: ";
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
    std::cout << "vertices:\n";
    for (auto it = graphs[index].second.vertices_begin(); it != graphs[index].second.vertices_end(); ++it)
        std::cout << *it << "\n";
    std::cout << "\n";
}

void check_if_edge_exists(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    int from, to;
    std::cout << "vertex1: "; std::cin >> from;
    std::cout << "vertex2: "; std::cin >> to;
    if (graphs[index].second.is_edge(from, to)) std::cout << "edge exists\n";
    else std::cout << "edge does not exist\n";
}

void get_degrees(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    int vertex;
    std::cout << "vertex: "; std::cin >> vertex;
    try {
        int in_degree = graphs[index].second.in_degree(vertex);
        int out_degree = graphs[index].second.out_degree(vertex);
        std::cout << "in degree: " << in_degree << "\n";
        std::cout << "out degree: " << out_degree << "\n";
    } catch (std::out_of_range& e) {
        std::cout << "vertex does not exist\n";
    }
}

void parse_outbound(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    int vertex;
    std::cout << "vertex: "; std::cin >> vertex;
    try {
        std::cout << "outbound edges:\n";
        for (auto it = graphs[index].second.outbound_begin(vertex); it != graphs[index].second.outbound_end(vertex); ++it)
            std::cout << *it << "\n";
        std::cout << "\n";
    } catch (std::out_of_range& e) {
        std::cout << "vertex does not exist\n";
    }
}

void parse_inbound(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    int vertex;
    std::cout << "vertex: "; std::cin >> vertex;
    try {
        std::cout << "inbound edges:\n";
        for (auto it = graphs[index].second.inbound_begin(vertex); it != graphs[index].second.inbound_end(vertex); ++it)
            std::cout << *it << "\n";
        std::cout << "\n";
    } catch (std::out_of_range& e) {
        std::cout << "vertex does not exist\n";
    }
}

void get_edge_cost(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    int from, to;
    std::cout << "vertex1: "; std::cin >> from;
    std::cout << "vertex2: "; std::cin >> to;
    try {
        int cost = graphs[index].second.get_edge_cost(from, to);
        std::cout << "cost: " << cost << "\n";
    } catch (std::out_of_range& e) {
        std::cout << "edge does not exist\n";
    }
}

void modify_edge_cost(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    int from, to, cost;
    std::cout << "vertex1: "; std::cin >> from;
    std::cout << "vertex2: "; std::cin >> to;
    std::cout << "cost: "; std::cin >> cost;
    try {
        graphs[index].second.modify_edge_cost(from, to, cost);
        std::cout << "cost modified\n";
    } catch (std::out_of_range& e) {
        std::cout << "edge does not exist\n";
    }
}

void add_vertex(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    int vertex;
    std::cout << "vertex: "; std::cin >> vertex;
    if (graphs[index].second.add_vertex(vertex)) std::cout << "vertex added\n";
    else std::cout << "vertex already exists\n";
}

void remove_vertex(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    int vertex;
    std::cout << "vertex: "; std::cin >> vertex;
    if (graphs[index].second.remove_vertex(vertex)) std::cout << "vertex removed\n";
    else std::cout << "vertex does not exist\n";
}

void add_edge(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    int from, to, cost;
    std::cout << "vertex1: "; std::cin >> from;
    std::cout << "vertex2: "; std::cin >> to;
    std::cout << "cost: "; std::cin >> cost;
    try {
        bool temp = graphs[index].second.add_edge(from, to, cost);
        if (temp == false) std::cout << "edge already exists, modified its cost\n";
        else std::cout << "edge added\n";
    } catch (std::out_of_range& e) {
        std::cout << "vertex does not exist\n";
    }
}

void remove_edge(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    int from, to;
    std::cout << "vertex1: "; std::cin >> from;
    std::cout << "vertex2: "; std::cin >> to;
    if (graphs[index].second.remove_edge(from, to)) std::cout << "edge removed\n";
    else std::cout << "edge does not exist\n";
}

void create_copy(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    graphs.emplace_back(graphs[index].first + "_copy", graphs[index].second.copy_graph());
}

void read_graph_from_file(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    std::string filename;
    std::cout << "filename: "; std::cin >> filename;
    try {
        graphs.emplace_back(filename, read_graph_from_file(filename));
    } catch (std::exception& e) {
        std::cout << "error reading graph from file: " << e.what() << "\n";
    }
}

void write_graph_to_file(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    std::string filename;
    std::cout << "filename: "; std::cin >> filename;
    try {
        write_graph_to_file(graphs[index].second, filename);
    } catch (std::exception& e) {
        std::cout << "error writing graph to file: " << e.what() << "\n";
    }
}

void create_random_graph(std::vector<std::pair<std::string, DirectedGraph>>& graphs, int index) {
    int vertex_count, edge_count;
    std::cout << "vertex count: "; std::cin >> vertex_count;
    std::cout << "edge count: "; std::cin >> edge_count;
    std::string graph_name;
    std::cout << "graph name: "; std::cin >> graph_name;
    try {
        graphs.emplace_back(graph_name, generate_random_graph(vertex_count, edge_count));
    }
    catch (std::exception& e) {
        std::cout << "error creating random graph: " << e.what() << "\n";
    }
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
            case 0: {
                return;
            }
            case 1: {
                int temp = switch_graph(graphs, index);
                if(temp != -1) index = temp;
                break;
            }
            case 2: {
                get_number_of_vertices(graphs, index);
                break;
            }
            case 3: {
                parse_vertices(graphs, index);
                break;
            }
            case 4: {
                check_if_edge_exists(graphs, index);
                break;
            }
            case 5: {
                get_degrees(graphs, index);
                break;
            }
            case 6: {
                parse_outbound(graphs, index);
                break;
            }
            case 7: {
                parse_inbound(graphs, index);
                break;
            }
            case 8: {
                get_edge_cost(graphs, index);
                break;
            }
            case 9: {
                modify_edge_cost(graphs, index);
                break;
            }
            case 10: {
                add_vertex(graphs, index);
                break;
            }
            case 11: {
                remove_vertex(graphs, index);
                break;
            }
            case 12: {
                add_edge(graphs, index);
                break;
            }
            case 13: {
                remove_edge(graphs, index);
                break;
            }
            case 14: {
                create_copy(graphs, index);
                break;
            }
            case 15: {
                read_graph_from_file(graphs, index);
                break;
            }
            case 16: {
                write_graph_to_file(graphs, index);
                break;
            }
            case 17: {
                create_random_graph(graphs, index);
                break;
            }
            default: {
                std::cout << "please enter a valid option\n";
                break;
            }
        }
    }
}

int main() {
    //test_graph();
    //std::cout << "tests ran succesfully\n\n";
    run_ui();
    system("pause");
    return 0;
}
