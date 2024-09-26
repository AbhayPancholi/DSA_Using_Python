# class Graph:
#     def __init__(self, gdict=None) -> None:
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict

#     def addEdge(self, vertex, edge):
#         self.gdict[vertex].append(edge)


# customdict = {
#     "a": ["b", "c"],
#     "b": ["a", "d", "e"],
#     "c": ["a", "e"],
#     "d": ["b", "e", "f"],
#     "e": ["d", "f"],
#     "f": ["d", "e"],
# }

# newGraph = Graph(customdict)
# newGraph.addEdge("e", "c")
# print(newGraph.gdict)


class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def printGraph(self):
        for vertex in self.adjacency_list.keys():
            print(vertex, ":", self.adjacency_list[vertex])


custGraph = Graph()
custGraph.addVertex("A")
custGraph.printGraph()
