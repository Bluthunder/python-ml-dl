"""
Adjancency List Implemenentation of Graph
"""

from collections import deque

class Graph():

    def __init__(self):
        self.adjacency_list = {}


    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = [] # empty list edge will be added
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex2)
            return True

        return False


    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex2)
            return True

        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)

            del self.adjacency_list[vertex]
            return True
        return False


    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f'{vertex}: {self.adjacency_list[vertex]}')


    #We use queue

    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)

        # queue = [vertex]
        queue = deque([vertex])

        while queue:
            # current_vertex = queue.pop(0)
            current_vertex = queue.popleft() # O(1) time pop using deque
            print(current_vertex)

            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)


    # We use stack
    def dfs(self, vertex):
        visited = set()
        stack = [vertex]

        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)

            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)




CG = Graph()
CG.add_vertex("A")
CG.add_vertex("B")
CG.add_vertex("C")
CG.add_vertex("D")
CG.add_vertex("E")
CG.add_edge("A", "B")
CG.add_edge("A", "C")
CG.add_edge("C","D")
CG.add_edge("B", "E")
CG.add_edge("D", "E")
print(f"------ADJACENCY LIST------ \n")
CG.print_graph()
print(f'BFS -----')
CG.bfs("A")
print(f'DFS -----')
CG.dfs("A")
