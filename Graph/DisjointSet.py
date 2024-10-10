class DisjointSet:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v

        self.rank = dict.fromkeys(vertices, 0)
