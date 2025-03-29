#pragma once
#include <map>
#include <vector>
#include <stdexcept>
#include <algorithm>

class DirectedGraph {
private:
    std::map<int, std::vector<int>> d_in;
    std::map<int, std::vector<int>> d_out;
    std::map<std::pair<int, int>, int> costs;
public:
    DirectedGraph() = default;
    explicit DirectedGraph(int vertex_count);
    explicit DirectedGraph(std::vector<int> vertices);
    DirectedGraph(const DirectedGraph& other);

    using VertexIterator = std::map<int, std::vector<int>>::const_iterator;
    using EdgeIterator = std::vector<int>::const_iterator;
    int vertex_count() const;
    VertexIterator vertices_begin();
    VertexIterator vertices_end();
    bool is_edge(int from, int to) const;
    int in_degree(int vertex);
    int out_degree(int vertex);
    EdgeIterator outbound_begin(int vertex);
    EdgeIterator outbound_end(int vertex);
    EdgeIterator inbound_begin(int vertex);
    EdgeIterator inbound_end(int vertex);
    int get_edge_cost(int from, int to);
    void modify_edge_cost(int from, int to, int cost);
    bool add_edge(int from, int to, int cost);
    bool remove_edge(int from, int to);
    bool add_vertex(int vertex);
    bool remove_vertex(int vertex);
    DirectedGraph copy_graph() const;
};