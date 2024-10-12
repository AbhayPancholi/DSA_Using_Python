import sys


class Graph:
    def __init__(self, nodes, edges, VertexNum) -> None:
        self.nodes = nodes
        self.edges = edges
        self.VertexNum = VertexNum
        self.MST = []

    def printSolution(self):
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s -> %s: %s" % (s, d, w))

    def primsAlgo(self):
        visited = [0] * self.VertexNum
        edgeNum = 0
        visited[0] = True

        while edgeNum < self.VertexNum - 1:
            min = sys.maxsize
            for i in range(self.VertexNum):
                if visited[i]:
                    for j in range(self.VertexNum):
                        if (not visited[j]) and self.edges[i][j]:
                            if min > self.edges[i[j]]:
                                min = self.edges[i][j]
                                s = i
                                d = j
            self.MST.append(self.node[s], self.node[d], self.edges[s][d])
            visited[d] = True
            edgeNum += 1
