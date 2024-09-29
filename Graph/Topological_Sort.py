from collections import defaultdict


class Graph:
    def __init__(self, numberOfVertices) -> None:
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)

        for vertex in self.graph[v]:
            if vertex not in visited:
                self.topologicalSortUtil(vertex, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)
        print(stack)


custGraph = Graph(8)

custGraph.addEdge("A", "C")
custGraph.addEdge("C", "E")
custGraph.addEdge("E", "H")
custGraph.addEdge("E", "F")
custGraph.addEdge("F", "G")
custGraph.addEdge("B", "D")
custGraph.addEdge("B", "C")
custGraph.addEdge("D", "F")

custGraph.topologicalSort()
