#include "DirectedGraph.h"
#include <iostream>
#include <fstream>
#include <sstream>

DirectedGraph::DirectedGraph(const int vertex_count) {
    for (int i=0; i<vertex_count; i++) {
        d_in[i] = std::vector<int>();
        d_out[i] = std::vector<int>();
    }
}

DirectedGraph::DirectedGraph(std::vector<int> vertices) {
    for (const auto& vertex : vertices) {
        d_in[vertex] = std::vector<int>();
        d_out[vertex] = std::vector<int>();
    }
}

DirectedGraph::DirectedGraph(DirectedGraph const& other) {
    d_in = other.d_in;
    d_out = other.d_out;
    costs = other.costs;
}

int DirectedGraph::vertex_count() const {
    return d_in.size();
}

bool DirectedGraph::is_edge(int from, int to) const {
    return costs.count({from, to}) > 0;
}

int DirectedGraph::in_degree(const int vertex) {
    if (d_in.count(vertex) == 0) return -1;
    return d_in[vertex].size();
}

int DirectedGraph::out_degree(const int vertex) {
    if (d_out.count(vertex) == 0) return -1;
    return d_out[vertex].size();
}

DirectedGraph::EdgeIterator DirectedGraph::outbound_begin(int vertex) {
    if (d_out.count(vertex) == 0) throw std::out_of_range("Vertex not found");
    return d_out[vertex].cbegin();
}

DirectedGraph::EdgeIterator DirectedGraph::outbound_end(int vertex) {
    if (d_out.count(vertex) == 0) throw std::out_of_range("Vertex not found");
    return d_out[vertex].cend();
}

DirectedGraph::EdgeIterator DirectedGraph::inbound_begin(int vertex) {
    if (d_in.count(vertex) == 0) throw std::out_of_range("Vertex not found");
    return d_in[vertex].cbegin();
}

DirectedGraph::EdgeIterator DirectedGraph::inbound_end(int vertex) {
    if (d_in.count(vertex) == 0) throw std::out_of_range("Vertex not found");
    return d_in[vertex].cend();
}

int DirectedGraph::get_edge_cost(int from, int to) {
    if (costs.count({from, to}) == 0) throw std::out_of_range("Edge not found");
    return costs[{from, to}];
}

void DirectedGraph::modify_edge_cost(int from, int to, int cost) {
    if (costs.count({from, to}) == 0) throw std::out_of_range("Edge not found");
    costs[{from, to}] = cost;
}

bool DirectedGraph::add_edge(int from, int to, int cost) {
    if (d_in.count(from) == 0 || d_out.count(to) == 0) throw std::out_of_range("Vertex not found");
    if (costs.count({from, to}) > 0) {
        costs[{from, to}] = cost;
        return false;
    }
    d_out[from].push_back(to);
    d_in[to].push_back(from);
    costs[{from, to}] = cost;
    return true;
}

bool DirectedGraph::remove_edge(int from, int to) {
    if (costs.count({from, to}) == 0) return false;
    costs.erase({from, to});
    std::remove(d_out[from].begin(), d_out[from].end(), to);
    std::remove(d_in[to].begin(), d_in[to].end(), from);
    return true;
}

bool DirectedGraph::add_vertex(int vertex) {
    if (d_in.count(vertex) > 0) return false;
    d_in[vertex] = std::vector<int>();
    d_out[vertex] = std::vector<int>();
    return true;
}

bool DirectedGraph::remove_vertex(int vertex) {
    if (d_in.count(vertex) == 0) return false;
    for (const auto& out_vertex : d_out[vertex]) {
        costs.erase({vertex, out_vertex});
        std::remove(d_in[out_vertex].begin(), d_in[out_vertex].end(), vertex);
    }
    for (const auto& in_vertex : d_in[vertex]) {
        costs.erase({in_vertex, vertex});
        std::remove(d_out[in_vertex].begin(), d_out[in_vertex].end(), vertex);
    }
    d_in.erase(vertex);
    d_out.erase(vertex);
    return true;
}

DirectedGraph DirectedGraph::copy_graph() const {
    DirectedGraph copy;
    copy.d_in = d_in;
    copy.d_out = d_out;
    copy.costs = costs;
    return copy;
}

DirectedGraph read_graph_from_file(const std::string& filename) {
    std::ifstream f(filename);
    if(!f.is_open()) throw std::runtime_error("File not found");
    std::string line; f >> line;
    if(line == "nodelist") {
        f.ignore();
        std::getline(f, line);
        std::vector<int> nodes;
        std::istringstream iss(line);
        int node;
        while (iss >> node) {
            nodes.push_back(node);
            //std::cout << node << " ";
        }
        std::cout << std::endl;
        DirectedGraph g(nodes);
        while (std::getline(f, line)) {
            std::istringstream iss2(line);
            int from, to, cost;
            if (iss2 >> from >> to >> cost) {
                g.add_edge(from, to, cost);
                //std::cout << from << " " << to << " " << cost << std::endl;
            }
        }
        return g;
    }
    int vertex_count = std::stoi(line);
    int edge_count; f >> edge_count;
    DirectedGraph g(vertex_count);
    for(int i=0; i<edge_count; i++) {
        int from, to, cost;
        f >> from >> to >> cost;
        g.add_edge(from, to, cost);
    }
    return g;
}

void write_graph_to_file(DirectedGraph &graph, const std::string &filename) {
    std::ofstream f(filename);
    f << "nodelist\n";
    for (auto it = graph.vertices_begin(); it != graph.vertices_end(); ++it)
        f << *it << " ";
    f << "\n";
    for (auto it = graph.vertices_begin(); it != graph.vertices_end(); ++it) {
        int vertex = *it;
        for (auto out_it = graph.outbound_begin(vertex); out_it != graph.outbound_end(vertex); ++out_it) {
            int to = *out_it;
            f << vertex << " " << to << " " << graph.get_edge_cost(vertex, to) << "\n";
        }
    }
}
