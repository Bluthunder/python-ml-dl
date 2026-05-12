
from typing import List
from collections import deque

def maximum_sliding_window(nums: List[int], k:int) -> List[int]:

    result = []
    d = deque()
    l = r = 0

    while r < len(nums):

        # remove smaller values from d
        while d and nums[d[-1]] < nums[r]:
            d.pop()

        d.append(r)

        # remove left val from window
        if d and d[0] < l:
            d.popleft()

        if (r + 1) >= k:
            result.append(nums[d[0]])
            l += 1

        r += 1

    return result


if __name__ == '__main__':

    nums = [1,3,-1,-3,5,3,6,7]

    k = 3

    print(maximum_sliding_window(nums, k))
