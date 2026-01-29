
from typing import List

# Brute Force
def two_sum_bf(nums: List[int], target: int)-> List[int]:

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]




def two_sum_optimized(nums: List[int], target: int)-> List[int]:
    seen = {}

    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

    return []




if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    print(two_sum_bf(nums, target))

    print(two_sum_optimized(nums, target))
