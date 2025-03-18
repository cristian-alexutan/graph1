from graph import DirectedGraph, GraphError, read_graph_from_file, write_graph_to_file, random_graph

def print_menu():
    print("")
    print("1 - print graph")
    print("2 - add vertex")
    print("3 - remove vertex")
    print("4 - add edge")
    print("5 - remove edge")
    print("6 - update edge")
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

def main():
    options = {
        "1": print_graph,
        "2": add_vertex,
        "3": remove_vertex,
        "4": add_edge,
        "5": remove_edge,
        "6": update_edge
    }

    g = read_graph_from_file("graph.txt")
    while True:
        print_menu()
        opt = input(" >>> ")
        opt = opt.strip()
        if opt == "0":
            break
        if opt not in options:
            print("please enter a valid option...")
            continue
        options[opt](g)

if __name__ == '__main__':
    main()