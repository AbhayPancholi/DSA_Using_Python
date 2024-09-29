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

from collections import deque


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

    def addEdge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def removeEdge(self, vertex1, vertex2):
        """The try-except block is added so that if someone tries to remove a vertex without any edges
        the error is not raised."""
        if vertex1 and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False

    def removeVertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)


custGraph = Graph()
custGraph.addVertex("A")
custGraph.addVertex("B")
custGraph.addVertex("C")
custGraph.addVertex("D")
custGraph.addVertex("E")
custGraph.addEdge("A", "B")
custGraph.addEdge("A", "C")
custGraph.addEdge("B", "E")
custGraph.addEdge("D", "E")
custGraph.addEdge("C", "D")
# custGraph.removeVertex("A")
# custGraph.printGraph()
custGraph.bfs("A")
