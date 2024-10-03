# class for edges
class Egde:
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


a = Node("A")
b = Node("B")
print(a > b)
