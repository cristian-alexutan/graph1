#include "DirectedGraph.h"
#include <stdexcept>
#include <algorithm>

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

DirectedGraph::VertexIterator DirectedGraph::vertices_begin() {
    return d_in.begin();
}

DirectedGraph::VertexIterator DirectedGraph::vertices_end() {
    return d_in.end();
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
    return d_out[vertex].begin();
}

DirectedGraph::EdgeIterator DirectedGraph::outbound_end(int vertex) {
    if (d_out.count(vertex) == 0) throw std::out_of_range("Vertex not found");
    return d_out[vertex].end();
}

DirectedGraph::EdgeIterator DirectedGraph::inbound_begin(int vertex) {
    if (d_in.count(vertex) == 0) throw std::out_of_range("Vertex not found");
    return d_in[vertex].begin();
}

DirectedGraph::EdgeIterator DirectedGraph::inbound_end(int vertex) {
    if (d_in.count(vertex) == 0) throw std::out_of_range("Vertex not found");
    return d_in[vertex].end();
}

int DirectedGraph::get_edge_cost(int from, int to) const {
    if (costs.count({from, to}) == 0) throw std::out_of_range("Edge not found");
    return costs.at({from, to});
}

void DirectedGraph::modify_edge_cost(int from, int to, int cost) {
    if (costs.count({from, to}) == 0) throw std::out_of_range("Edge not found");
    costs[{from, to}] = cost;
}

bool DirectedGraph::add_edge(int from, int to, int cost) {
    if (d_in.count(from) == 0 || d_out.count(to) == 0) throw std::out_of_range("Vertex not found");
    if (costs.count({from, to}) == 0) {
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
    return true;
}

DirectedGraph DirectedGraph::copy_graph() const {
    DirectedGraph copy;
    copy.d_in = d_in;
    copy.d_out = d_out;
    copy.costs = costs;
    return copy;
}