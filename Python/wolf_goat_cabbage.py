class GraphError(Exception):
    pass

class DirectedGraph:
    def __init__(self):
        self._d_out = {}

    def add_vertex(self, vertex: int) -> bool:
        if vertex not in self._d_out:
            self._d_out[vertex] = []
            return True
        return False

    def add_edge(self, vertex1: int, vertex2: int) -> bool:
        if vertex1 not in self._d_out:
            raise GraphError("vertex doesn't exist")
        if vertex2 not in self._d_out:
            raise GraphError("vertex doesn't exist")
        if vertex2 in self._d_out[vertex1]:
            return False
        self._d_out[vertex1].append(vertex2)
        return True

    def outbound(self, vertex: int) -> iter:
        if vertex not in self._d_out:
            raise GraphError("vertex does not exist")
        return iter(self._d_out[vertex])

def valid(mask: int) -> bool:
    left = mask
    right = ~mask
    # wolf and goat on the same bank without the human
    if (left & 0b0001) and (left & 0b0010) and not (left & 0b1000):
        return False
    if (right & 0b0001) and (right & 0b0010) and not (right & 0b1000):
        return False
    # goat and cabbage on the same bank without the human
    if (left & 0b0010) and (left & 0b0100) and not (left & 0b1000):
        return False
    if (right & 0b0010) and (right & 0b0100) and not (right & 0b1000):
        return False
    return True

def bfs(graph: DirectedGraph, start: int, end: int):
    queue = [start]
    distance = {start: 0}
    previous = {start: None}
    while queue:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in graph.outbound(current):
            if neighbor not in distance:
                distance[neighbor] = distance[current] + 1
                previous[neighbor] = current
                queue.append(neighbor)
    return distance, previous

def print_state(state: int):
    wolf = "wolf" if state & 0b0001 else ""
    goat = "goat" if state & 0b0010 else ""
    cabbage = "cabbage" if state & 0b0100 else ""
    human = "human" if state & 0b1000 else ""
    if wolf == "" and goat == "" and cabbage == "" and human == "":
        print("left bank is empty")
    else:
        print(f"{wolf} {goat} {cabbage} {human} on the left bank")
    wolf = "wolf" if ~state & 0b0001 else ""
    goat = "goat" if ~state & 0b0010 else ""
    cabbage = "cabbage" if ~state & 0b0100 else ""
    human = "human" if ~state & 0b1000 else ""
    if wolf == "" and goat == "" and cabbage == "" and human == "":
        print("right bank is empty")
    else:
        print(f"{wolf} {goat} {cabbage} {human} on the right bank")

def main():
    # wolf goat cabbage problem
    # each node represents a state
    # states are hashed to a bitmask with 4 bits "mask"
    # mask - the state of the left bank
    # ~mask - the state of the right bank
    # for both masks, the following bits represent:
    # bit 0 - wolf
    # bit 1 - goat
    # bit 2 - cabbage
    # bit 3 - human
    # we start from the state 1111 (all on the left bank)
    # and end at the state 0000 (all on the right bank)
    g = DirectedGraph()
    for state1 in range(16):
        if valid(state1):
            g.add_vertex(state1)
    for state1 in range(16):
        if valid(state1):
            state2 = state1 ^ 0b1000
            if valid(state2):
                g.add_edge(state1, state2)
            for bit in range(3):
                state2 = state1 ^ (1 << bit) ^ 0b1000
                if valid(state2):
                    g.add_edge(state1, state2)
    distance, previous = bfs(g, 0b1111, 0b0000)
    path = []
    current = 0b0000
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    print("solution:")
    for state in path:
        print_state(state)
        print()
    print(f"{distance[0000]} steps")

if __name__ == "__main__":
    main()