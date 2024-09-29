from collections import defaultdict


class Graph:
    def __init__(self, numberOfVertices) -> None:
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices
