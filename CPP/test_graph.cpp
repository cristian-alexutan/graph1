#include "DirectedGraph.h"
#include "test_graph.h"
#include <cassert>
#include <iostream>

void test_graph() {
    DirectedGraph g(5);
    assert(g.vertex_count() == 5);
    assert(g.add_edge(0, 1, 10));
    assert(g.add_edge(1, 2, 20));
    assert(g.add_edge(2, 3, 30));
    assert(g.add_edge(3, 4, 40));
    assert(!g.add_edge(0, 1, 50)); // Edge already exists
    assert(g.get_edge_cost(0, 1) == 50);
    g.modify_edge_cost(0, 1, 15);
    assert(g.get_edge_cost(0, 1) == 15);
    assert(g.in_degree(1) == 1);
    assert(g.out_degree(1) == 1);
    assert(g.is_edge(0, 1));
    assert(!g.is_edge(1, 0));
    g.remove_edge(0, 1);
    assert(!g.is_edge(0, 1));
    assert(g.add_vertex(5));
    assert(g.add_edge(5, 0, 25));
    assert(g.get_edge_cost(5, 0) == 25);
    assert(g.remove_vertex(5));
    assert(!g.is_edge(5, 0));
    assert(g.remove_edge(1, 2));
    assert(!g.is_edge(1, 2));
    assert(g.remove_edge(2, 3));
    assert(!g.is_edge(2, 3));
}