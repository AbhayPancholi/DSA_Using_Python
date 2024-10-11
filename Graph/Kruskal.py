class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []
        self.node = []
        self.MST = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
