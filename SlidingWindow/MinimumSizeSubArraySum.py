
from typing import List

def min_sub_array_len(s: int, nums:List[int])->int:
    min_length = float('inf')

    start = 0
    total = 0

    for end in range(len(nums)):
        total += nums[end]

        while total >= s:
            min_length = min(min_length, end-start+1)
            total -= nums[start]
            start += 1

    return 0 if min_length == float('inf') else int(min_length)



if __name__ == '__main__':

    nums = [2,3,1,2,4,3]
    s = 7

    print(min_sub_array_len(s, nums))
