
class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.adjMatrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adjMatrix[u][v] = 1
        self.adjMatrix[v][u] = 1


    def remove_edge(self, u, v):
        self.adjMatrix[u][v] = 0
        self.adjMatrix[v][u] = 0

    def print_matrix(self):
        for row in self.adjMatrix:
            print(row)


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(3, 1)

g.print_matrix()
