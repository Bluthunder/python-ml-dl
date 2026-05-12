
from typing import List


def can_visit_all_rooms(rooms: List[List[int]])-> bool:

    visited = set()
    stack = [0]

    while stack:
        room = stack.pop()

        if room in visited:
            continue
        visited.add(room)

        for keys in rooms[room]:
            if keys not in visited:
                stack.append(keys)


    return len(visited) == len(rooms)



if __name__ == '__main__':

    rooms = [[1,3], [3, 0, 1], [2], [0]]

    print(can_visit_all_rooms(rooms))
