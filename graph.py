from __future__ import annotations
from random import randint


class GraphError(Exception):
    pass

class DirectedGraph:
    def __init__(self, d_in = None, d_out = None, costs = None):
        if d_in is None:
            self._d_in = {}
        else:
            self._d_in = d_in
        if d_out is None:
            self._d_out = {}
        else:
            self._d_out = d_out
        if costs is None:
            self._costs = {}
        else:
            self._costs = costs

    def add_vertex(self, vertex: int) -> None:
        if vertex not in self._d_in:
            self._d_in[vertex] = []
            self._d_out[vertex] = []

    def remove_vertex(self, vertex: int) -> None:
        if vertex not in self._d_in:
            raise GraphError("vertex not found")
        for out in self._d_out[vertex]:
            self._costs.pop(vertex, out)
            self._d_in[out].remove(vertex)
        self._d_out.pop(vertex)

    def add_edge(self, vertex1: int, vertex2: int, cost: int) -> None:
        if vertex1 not in self._d_in:
            self.add_vertex(vertex1)
        if vertex2 not in self._d_in:
            self.add_vertex(vertex2)
        if (vertex1, vertex2) in self._costs:
            raise GraphError("edge already exists")
        self._costs[(vertex1, vertex2)] = cost
        self._d_out[vertex1].append(vertex2)
        self._d_in[vertex2].append(vertex1)

    def remove_edge(self, vertex1: int, vertex2: int) -> None:
        if (vertex1, vertex2) not in self._costs:
            raise GraphError("edge does not exist")
        self._costs.pop((vertex1, vertex2))

    def vertices(self) -> iter:
        return iter(self._d_in.keys())

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        return vertex2 in self._d_in[vertex1]

    def in_degree(self, vertex: int) -> int:
        if vertex not in self._d_in:
            raise GraphError("vertex does not exist")
        return len(self._d_in[vertex])

    def out_degree(self, vertex: int) -> int:
        if vertex not in self._d_out:
            raise GraphError("vertex does not exist")
        return len(self._d_out[vertex])

    def vertice_count(self) -> int:
        return len(self._d_in.keys())

    def edge_count(self) -> int:
        return len(self._costs)

    def outbound(self, vertex: int) -> iter:
        if vertex not in self._d_out:
            raise GraphError("vertex does not exist")
        return iter(self._d_out[vertex])

    def inbound(self, vertex: int) -> iter:
        if vertex not in self._d_in:
            raise GraphError("vertex does not exist")
        return iter(self._d_in[vertex])

    def get_cost(self, vertex1: int, vertex2: int):
        if (vertex1, vertex2) not in self._costs:
            raise GraphError("edge does not exist")
        return self._costs[(vertex1, vertex2)]

    def copy_graph(self) -> DirectedGraph:
        in_copy = self._d_in.copy()
        out_copy = self._d_out.copy()
        costs_copy = self._costs.copy()
        return DirectedGraph(in_copy, out_copy, costs_copy)

def read_graph_from_file(filename: str, g: DirectedGraph) -> None:
    with open(filename, "r") as f:
        lines = f.readlines()
        first = True
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            if first:
                first = False
                tokens = line.split()
                vertex_count = int(tokens[0])
                for i in range(vertex_count):
                    g.add_vertex(i)
                continue
            tokens = line.split()
            vertex1 = int(tokens[0])
            vertex2 = int(tokens[1])
            cost = int(tokens[2])
            g.add_edge(vertex1, vertex2, cost)

def write_graph_to_file(filename: str, g: DirectedGraph) -> None:
    print(f"{g.vertice_count(), g.edge_count()}")
    with open(filename, "w") as f:
        for vertex1 in range(g.vertice_count()):
            for vertex2 in g.outbound(vertex1):
                print(f"{vertex1} {vertex2} {g.get_cost(vertex1, vertex2)}", file = f)

def random_graph(vertices: int, edges: int) -> DirectedGraph:
    g = DirectedGraph()
    for i in range(vertices):
        g.add_vertex(i)
    for i in range(edges):
        vertex1 = randint(0, g.vertice_count() - 1)
        vertex2 = randint(0, g.vertice_count() - 1)
        cost = randint(-100, 100)
        g.add_edge(vertex1, vertex2, cost)
    return g