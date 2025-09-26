# Incomplete

class Vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False


    def addNeighbour(self, neigbhour, G):
        G.addEdge(self.id, neigbhour)

    def getConnections(self, G):
        return G.adjMatrix[self.id]

    def getVertex_ID(self):
        return self.id

    def setVertex_ID(self, id):
        self.id = id

    def __str__(self):
        return str(self.id)


class Graph:

    def __init__(self, numVertices, cost = 0):
        self.adjMatrix = [[-1] * numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for in range(0, numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)

    def setVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertex_ID(id)

    def getVertex(self, n):
        for ve
