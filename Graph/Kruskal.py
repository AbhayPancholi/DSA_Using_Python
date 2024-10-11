class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []
        self.node = []
        self.MST = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def add_node(self, value):
        self.nodes.append(value)

    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))
