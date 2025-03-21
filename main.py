from graph import DirectedGraph, GraphError, read_graph_from_file, write_graph_to_file, random_graph

def print_menu():
    print("")
    print("1 - print graph")
    print("2 - add vertex")
    print("3 - remove vertex")
    print("4 - add edge")
    print("5 - remove edge")
    print("6 - update edge")
    print("7 - print outbound neighbors of vertex")
    print("8 - in degree")
    print("9 - out degree")
    print("10 - read graph from file")
    print("11 - write graph to file")
    print("12 - get edge value")
    print("13 - print inbound")
    print("14 - generate random graph")
    print("15 - number of vertices in graph")
    print("16 - check if edge exists")
    print("0 - exit")
    print("=================")

def print_graph(g: DirectedGraph):
    for u in g.vertices():
        ans = f"{u}: "
        for v in g.outbound(u):
            ans += f"{v} "
        print(ans)

def add_vertex(g: DirectedGraph):
    v = input("vertex: ")
    if not v.isdigit():
        print("please enter a valid vertex")
        return
    v = int(v)
    if not g.add_vertex(v):
        print("vertex already exists")

def remove_vertex(g: DirectedGraph):
    v = input("vertex: ")
    if not v.isdigit():
        print("please enter a valid vertex")
        return
    v = int(v)
    try:
        g.remove_vertex(v)
    except GraphError as e:
        print(e)

def read_edge(cost: False) -> tuple:
    vertex1 = input("vertex1: ")
    if not vertex1.isdigit():
        print("please enter a valid vertex")
        return None, None, None
    vertex1 = int(vertex1)
    vertex2 = input("vertex2: ")
    if not vertex2.isdigit():
        print("please enter a valid vertex")
        return None, None, None
    vertex2 = int(vertex2)
    if not cost: return vertex1, vertex2
    cost = input("cost: ")
    if not cost.isdigit():
        print("please enter a valid cost")
        return None, None, None
    cost = int(cost)
    return vertex1, vertex2, cost

def add_edge(g: DirectedGraph):
    vertex1, vertex2, cost = read_edge(True)
    if vertex1 is None:
        return
    if not g.add_edge(vertex1, vertex2, cost):
        print("edge already exists")

def remove_edge(g: DirectedGraph):
    vertex1, vertex2 = read_edge(False)
    if vertex1 is None:
        return
    try:
        g.remove_edge(vertex1, vertex2)
    except GraphError as e:
        print(e)

def update_edge(g: DirectedGraph):
    vertex1, vertex2, cost = read_edge(True)
    if vertex1 is None:
        return
    try:
        g.modify_cost(vertex1, vertex2, cost)
    except GraphError as e:
        print(e)

def read_vertex():
    vertex = input("vertex: ")
    if not vertex.isdigit():
        print("please enter a valid vertex")
        return None
    return int(vertex)

def print_outbound(g: DirectedGraph):
    vertex = read_vertex()
    if vertex is None:
        return
    try:
        for x in g.outbound(vertex):
            print(x)
    except GraphError as e:
        print(e)

def in_degree(g: DirectedGraph):
    vertex = read_vertex()
    if vertex is None:
        return
    try:
        print(g.in_degree(vertex))
    except GraphError as e:
        print(e)

def out_degree(g: DirectedGraph):
    vertex = read_vertex()
    if vertex is None:
        return
    try:
        print(g.out_degree(vertex))
    except GraphError as e:
        print(e)

def write_to_file(g: DirectedGraph):
    file_name = input("file name: ")
    write_graph_to_file(file_name, g)

def get_edge_value(g: DirectedGraph):
    vertex1, vertex2 = read_edge(False)
    if vertex1 is None:
        return
    try:
        cost = g.get_cost(vertex1, vertex2)
        print(cost)
    except GraphError as e:
        print(e)

def print_inbound(g: DirectedGraph):
    vertex = read_vertex()
    if vertex is None:
        return
    try:
        for x in g.inbound(vertex):
            print(x)
    except GraphError as e:
        print(e)

def number_of_vertices(g: DirectedGraph):
    print(g.vertice_count())

def check_edge(g: DirectedGraph):
    vertex1, vertex2 = read_edge(False)
    if vertex1 is None:
        return
    print(g.is_edge(vertex1, vertex2))

def main():
    options = {
        "1": print_graph,
        "2": add_vertex,
        "3": remove_vertex,
        "4": add_edge,
        "5": remove_edge,
        "6": update_edge,
        "7": print_outbound,
        "8": in_degree,
        "9": out_degree,
        "11": write_to_file,
        "12": get_edge_value,
        "13": print_inbound,
        "15": number_of_vertices,
        "16": check_edge
    }

    g = DirectedGraph()
    while True:
        print_menu()
        opt = input(" >>> ")
        opt = opt.strip()
        if opt == "0":
            break
        if opt == "10":
            filename = input("file name: ")
            g = read_graph_from_file(filename)
            continue
        if opt == "14":
            vcnt = input("vertex count: ")
            vcnt = int(vcnt)
            ecnt = input("edge count: ")
            ecnt = int(ecnt)
            try:
                g = random_graph(vcnt, ecnt)
            except GraphError as e:
                print(e)
            continue
        if opt not in options:
            print("please enter a valid option...")
            continue
        options[opt](g)

if __name__ == '__main__':
    main()