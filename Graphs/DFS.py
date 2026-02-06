
from typing import Dict, List

import pdb


def dfs_recursive(node: str, graph: Dict[str, List[str]], visited: Dict[str, bool])->None:
    visited[node] = True
    print(node, end=' --> ')

    # breakpoint()

    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs_recursive(neighbour, graph, visited)



def dfs_iterative(start: str, graph: Dict[str, List[str]], visited: Dict[str, bool] ):

    # visited = [False] * len(graph)
    stack: List[str] = [start]

    # result: List[int] = []


    while stack:
        node = stack.pop()

        # breakpoint()

        if not visited[node]:
            visited[node] = True
            print(node, end = ' --> ')
            # result.append(node)

            for i in range(len(graph[node])-1, -1, -1):
                neighbour = graph[node][i]
                if not visited[neighbour]:
                    stack.append(neighbour)

    # return result




if __name__ == '__main__':

    graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : [],
        'F' : []
    }

    visited: Dict[str, bool] = {node: False for node in graph}

    # breakpoint()
    print(f'Recursive ')

    dfs_recursive('A', graph, visited)

    print(" ")

    visited: Dict[str, bool] = {node: False for node in graph}

    print(f'Iterative ')

    dfs_iterative('A', graph, visited)

    print(" ")
