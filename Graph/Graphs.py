class Graph:
    def __init__(self, gdict=None) -> None:
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


customdict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"],
}

newGraph = Graph(customdict)
newGraph.addEdge("e", "c")
print(newGraph.gdict)
