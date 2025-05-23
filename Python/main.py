from graph import DirectedGraph, GraphError, read_graph_from_file, write_graph_to_file, random_graph, connected_components, strongly_connected_components, biconnected_components

def print_menu():
    print()
    print("1 - select graph")
    print("2 - get number of vertices")
    print("3 - parse vertices")
    print("4 - check if edge exists")
    print("5 - get in degree / out degree of vertex")
    print("6 - parse outbound edges of vertex")
    print("7 - parse inbound edges of vertex")
    print("8 - get cost of edge")
    print("9 - modify cost of edge")
    print("10 - add vertex")
    print("11 - remove vertex")
    print("12 - add edge")
    print("13 - remove edge")
    print("14 - create copy of graph")
    print("15 - read graph from file")
    print("16 - write graph to file")
    print("17 - create random graph")
    print("18 - get connected components")
    print("19 - get strongly connected components")
    print("20 - get biconnected components")
    print("21 - get minimum cost walk")
    print("0 - exit")
    print("=========================================")

def read_vertex():
    while True:
        try:
            vertex = int(input("vertex: "))
            return vertex
        except ValueError:
            print("please enter an integer")

def read_edge():
    while True:
        try:
            vertex1 = int(input("vertex1: "))
            vertex2 = int(input("vertex2: "))
            return vertex1, vertex2
        except ValueError:
            print("please enter integers")

def select_graph(graphs: list, index: int) -> int:
    print(f"current graph: {graphs[index][0]}")
    print("available graphs:")
    for i, (name, _) in enumerate(graphs):
        print(f"{i} - {name}")
    while True:
        try:
            opt = int(input("enter graph index: "))
            if opt < 0 or opt >= len(graphs):
                raise ValueError
            return opt
        except ValueError:
            print("please select a valid graph")

def get_number_of_vertices(graphs: list, index: int):
    g = graphs[index][1]
    print(f"number of vertices: {g.vertice_count()}")

def parse_vertices(graphs: list, index: int):
    g = graphs[index][1]
    print("vertices:")
    for vertex in g.vertices():
        print(vertex)

def check_edge_exists(graphs: list, index: int):
    g = graphs[index][1]
    vertex1, vertex2 = read_edge()
    if g.is_edge(vertex1, vertex2):
        print(f"edge ({vertex1}, {vertex2}) exists")
    else:
        print(f"edge ({vertex1}, {vertex2}) does not exist")

def get_in_degree_out_degree(graphs: list, index: int):
    g = graphs[index][1]
    vertex = read_vertex()
    try:
        in_degree = g.in_degree(vertex)
        out_degree = g.out_degree(vertex)
    except GraphError as e:
        print(e)
        return
    print(f"vertex {vertex} in degree: {in_degree}")
    print(f"vertex {vertex} out degree: {out_degree}")

def parse_outbound_edges(graphs: list, index: int):
    g = graphs[index][1]
    vertex = read_vertex()
    print(f"outbound edges of vertex {vertex}:")
    try:
        for edge in g.outbound(vertex):
            print(edge)
    except GraphError as e:
        print(e)

def parse_inbound_edges(graphs: list, index: int):
    g = graphs[index][1]
    vertex = read_vertex()
    print(f"inbound edges of vertex {vertex}:")
    try:
        for edge in g.inbound(vertex):
            print(edge)
    except GraphError as e:
        print(e)

def get_cost_of_edge(graphs: list, index: int):
    g = graphs[index][1]
    vertex1, vertex2 = read_edge()
    try:
        cost = g.get_cost(vertex1, vertex2)
        print(f"cost of edge ({vertex1}, {vertex2}): {cost}")
    except GraphError as e:
        print(e)

def modify_cost_of_edge(graphs: list, index: int):
    vertex1, vertex2 = read_edge()
    cost = int(input("cost: "))
    try:
        graphs[index][1].modify_cost(vertex1, vertex2, cost)
    except GraphError as e:
        print(e)

def add_vertex(graphs: list, index: int):
    vertex = read_vertex()
    ans = graphs[index][1].add_vertex(vertex)
    if not ans:
        print("vertex already exists")

def remove_vertex(graphs: list, index: int):
    vertex = read_vertex()
    ans = graphs[index][1].remove_vertex(vertex)
    if not ans:
        print("vertex does not exist")

def add_edge(graphs: list, index: int):
    vertex1, vertex2 = read_edge()
    cost = int(input("cost: "))
    try:
        ans = graphs[index][1].add_edge(vertex1, vertex2, cost)
        if not ans:
            print("edge already exists")
    except GraphError as e:
        print(e)

def remove_edge(graphs: list, index: int):
    vertex1, vertex2 = read_edge()
    ans = graphs[index][1].remove_edge(vertex1, vertex2)
    if not ans:
        print("edge does not exist")

def create_copy_of_graph(graphs: list, index: int):
    copy = graphs[index][1].copy_graph()
    graphs.append((f"{graphs[index][0]}_copy", copy))

def read_from_file(graphs: list, index: int):
    filename = input("filename: ")
    try:
        g = read_graph_from_file(filename)
        graphs.append((filename, g))
    except GraphError as e:
        print(e)

def write_to_file(graphs: list, index: int):
    filename = input("filename: ")
    try:
        write_graph_to_file(filename, graphs[index][1])
    except GraphError as e:
        print(e)

def create_random_graph(graphs: list, index: int):
    vertices = int(input("number of vertices: "))
    edges = int(input("number of edges: "))
    graph_name = input("graph name: ")
    try:
        g = random_graph(vertices, edges)
        graphs.append((graph_name, g))
    except GraphError as e:
        print(e)

def get_connected_components(graphs: list, index: int):
    g = graphs[index][1]
    components = connected_components(g)
    for i in range(len(components)):
        print(f"component {i}: ")
        nodes = ""
        for node in components[i].vertices():
            nodes += str(node) + " "
        print(nodes)
    for i in range(len(components)):
        name = f"{graphs[index][0]}_comp_{i}"
        graphs.append((name, components[i]))

def get_strongly_connected_components(graphs: list, index: int):
    g = graphs[index][1]
    components = strongly_connected_components(g)
    for i in range(len(components)):
        print(f"component {i}: ")
        nodes = ""
        for node in components[i].vertices():
            nodes += str(node) + " "
        print(nodes)
    for i in range(len(components)):
        name = f"{graphs[index][0]}_comp_{i}"
        graphs.append((name, components[i]))

def get_biconnected_components(graphs: list, index: int):
    g = graphs[index][1]
    components = biconnected_components(g)
    for i in range(len(components)):
        print(f"component {i}: ")
        nodes = ""
        for node in components[i].vertices():
            nodes += str(node) + " "
        print(nodes)
    for i in range(len(components)):
        name = f"{graphs[index][0]}_comp_{i}"
        graphs.append((name, components[i]))

def min_cost_walk(graphs: list, index: int):
    g = graphs[index][1]
    vertex1 = int(input("vertex1: "))
    vertex2 = int(input("vertex2: "))
    try:
        cost, path = g.min_cost_walk(vertex1, vertex2)
        print(f"cost: {cost}")
        print(f"path: {path}")
    except GraphError as e:
        print(e)

def main():
    options = {
        "2": get_number_of_vertices,
        "3": parse_vertices,
        "4": check_edge_exists,
        "5": get_in_degree_out_degree,
        "6": parse_outbound_edges,
        "7": parse_inbound_edges,
        "8": get_cost_of_edge,
        "9": modify_cost_of_edge,
        "10": add_vertex,
        "11": remove_vertex,
        "12": add_edge,
        "13": remove_edge,
        "14": create_copy_of_graph,
        "15": read_from_file,
        "16": write_to_file,
        "17": create_random_graph,
        "18": get_connected_components,
        "19": get_strongly_connected_components,
        "20": get_biconnected_components,
        "21": min_cost_walk
    }

    g = DirectedGraph()
    graphs = [("graph1", g)]
    index = 0
    while True:
        print_menu()
        opt = input(" >>> ")
        opt = opt.strip()
        if opt == "0":
            break
        if opt == "1":
            index = select_graph(graphs, index)
            continue
        if opt not in options:
            print("please select a valid option")
            continue
        options[opt](graphs, index)

if __name__ == "__main__":
    main()