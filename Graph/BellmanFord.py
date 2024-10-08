class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print("Vertex distance form source")
        for key, val in dist.items():
            print("  " + key, " :  " + val)
