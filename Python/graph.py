from random import randint

class GraphError(Exception):
    pass

class DirectedGraph:
    def __init__(self, v = None, d_in = None, d_out = None, costs = None):
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
        if isinstance(v, int):
            for i in range(v):
                self.add_vertex(i)
        elif isinstance(v, list):
            for i in v:
                self.add_vertex(i)

    def add_vertex(self, vertex: int) -> bool:
        if vertex not in self._d_in:
            self._d_in[vertex] = []
            self._d_out[vertex] = []
            return True
        return False

    def remove_vertex(self, vertex: int) -> bool:
        if vertex not in self._d_in:
            return False
        for out in self._d_out[vertex]:
            self._costs.pop((vertex, out), None)
            self._d_in[out].remove(vertex)
        for node in self._d_in[vertex]:
            self._costs.pop((node, vertex), None)
            self._d_out[node].remove(vertex)
        self._d_in.pop(vertex, None)
        self._d_out.pop(vertex, None)
        return True

    def add_edge(self, vertex1: int, vertex2: int, cost: int) -> bool:
        if vertex1 not in self._d_in:
            raise GraphError("vertex doesn't exist")
        if vertex2 not in self._d_in:
            raise GraphError("vertex doesn't exist")
        if (vertex1, vertex2) in self._costs:
            return False
        self._costs[(vertex1, vertex2)] = cost
        self._d_out[vertex1].append(vertex2)
        self._d_in[vertex2].append(vertex1)
        return True

    def remove_edge(self, vertex1: int, vertex2: int) -> bool:
        if (vertex1, vertex2) not in self._costs.keys():
            return False
        self._costs.pop((vertex1, vertex2))
        self._d_out[vertex1].remove(vertex2)
        self._d_in[vertex2].remove(vertex1)
        return True

    def vertices(self) -> iter:
        return iter(self._d_in.keys())

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        if vertex1 not in self._d_in.keys() or vertex2 not in self._d_in.keys():
            return False
        if vertex2 in self._d_out[vertex1]:
            return True
        return False

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

    def get_cost(self, vertex1: int, vertex2: int) -> int:
        if (vertex1, vertex2) not in self._costs:
            raise GraphError("edge does not exist")
        return self._costs[(vertex1, vertex2)]

    def modify_cost(self, vertex1: int, vertex2: int, cost: int) -> None:
        if (vertex1, vertex2) not in self._costs:
            raise GraphError("vertex does not exist")
        self._costs[(vertex1, vertex2)] = cost

    def copy_graph(self) -> "DirectedGraph":
        in_copy = self._d_in.copy()
        out_copy = self._d_out.copy()
        costs_copy = self._costs.copy()
        return DirectedGraph(None, in_copy, out_copy, costs_copy)

def read_graph_from_file(filename: str) -> "DirectedGraph":
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        raise GraphError(f"file {filename} not found")
    with open(filename, "r") as f:
        line = f.readline()
        line = line.strip()
        tokens = line.split()
        edges = int(tokens[1])
        g = DirectedGraph()
        for i in range(edges):
            line = f.readline()
            line = line.strip()
            tokens = line.split()
            vertex1 = int(tokens[0])
            vertex2 = int(tokens[1])
            cost = int(tokens[2])
            g.add_vertex(vertex1)
            g.add_vertex(vertex2)
            g.add_edge(vertex1, vertex2, cost)
        iso = f.readline()
        if iso == "iso":
            line = f.readline()
            line = f.readline()
            for node in line.split():
                node = int(node)
                g.add_vertex(node)
        return g

def write_graph_to_file(filename: str, g: "DirectedGraph") -> None:
    with open(filename, "w") as f:
        f.write(f"{g.vertice_count()} {g.edge_count()}\n")
        iso = []
        for vertex1 in g.vertices():
            if g.in_degree(vertex1) == 0 and g.out_degree(vertex1) == 0:
                iso.append(vertex1)
            for vertex2 in g.outbound(vertex1):
                f.write(f"{vertex1} {vertex2} {g.get_cost(vertex1, vertex2)}\n")
        if len(iso) != 0:
            f.write("iso\n")
            f.write(f"{len(iso)}\n")
            for node in iso:
                f.write(f"{node} ")
            f.write("\n")

def random_graph(vertices: int, edges: int) -> "DirectedGraph":
    if edges > vertices ** 2:
        raise GraphError(f"can't create graph with {vertices} vertices and {edges} edges")
    g = DirectedGraph()
    for i in range(vertices):
        g.add_vertex(i)
    count = 0
    while count < edges:
        vertex1 = randint(0, g.vertice_count() - 1)
        vertex2 = randint(0, g.vertice_count() - 1)
        cost = randint(-100, 100)
        rez = g.add_edge(vertex1, vertex2, cost)
        count += rez
    return g