import heapq


# class for edges
class Edge:
    def __init__(self, weight, start_vertex, end_vertex) -> None:
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex


# class for nodes
class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.visited = None
        # previous node that we come to this node
        self.predecessor = None
        self.neighbours = []
        self.min_distance = float("inf")

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbours.append(edge)


class Dijkstra:
    def __init__(self) -> None:
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)

        while self.heap:
            # pop element with lowest distance
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # consider the neighbours
            for edge in actual_vertex.neighbours:
                start = edge.start_vertex
                target = edge.target_vertex

                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    # update the heap
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True

    def calculate(self, vertex):
        print(f"The shortest path to the vertex is: {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.predecessor
