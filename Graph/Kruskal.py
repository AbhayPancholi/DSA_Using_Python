import DisjointSet as dst


class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []
        self.node = []
        self.MST = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def add_node(self, value):
        self.node.append(value)

    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))

    def kruskalAlgo(self):
        i, e = 0, 0
        ds = dst.DisjointSet(self.node)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s, d, w])
                ds.union(x, y)
        self.printSolution(s, d, w)
