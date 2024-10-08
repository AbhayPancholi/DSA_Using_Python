class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print("Vertex distance form source")
        for key, val in dist.items():
            print("  " + key, " :  " + val)

    def bellman_ford(self, src):
        dist = {i: float("inf") for i in self.nodes}
        dist[src] = 0

        for i in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("inf") and dist[d] > dist[s] + w:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float("inf") and dist[d] > dist[s] + w:
                print("Graph contains negative cycle")
                return

        self.print_solution(dist)
