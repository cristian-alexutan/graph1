#include <iostream>
#include "DirectedGraph.h"
#include "test_graph.h"

int main() {
    std::cout << "Running tests\n";
    test_graph();
    std::cout << "All tests passed\n";
    system("pause");
    return 0;
}
