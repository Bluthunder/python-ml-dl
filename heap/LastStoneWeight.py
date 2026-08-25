from typing import List
import heapq



# Method using sorting
def lastStoneWeight(stones: List[int])->int:
    stones = list(stones)

    while len(stones) > 1 :
        stones.sort()
        x = stones.pop()
        y = stones.pop()

        if y != x:
            stones.append(x-y)

    return stones[0] if stones else 0



# Method using max heap, optimal
def lastStoneWeight_1(stones: List[int])-> int:

    heap = [-s for s in stones]

    heapq.heapify(heap)

    while len(heap) > 1:
        y = -heapq.heappop(heap)
        x = -heapq.heappop(heap)
        if y != x:
            heapq.heappush(heap, -(y - x))

    return -heap[0] if heap else 0



if __name__ == '__main__':

    stones = [2,7,4,1,8,1]

    print(lastStoneWeight(stones))

    print(lastStoneWeight_1(stones))
