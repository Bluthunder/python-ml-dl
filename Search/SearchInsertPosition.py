from typing import List

def searchInsert(nums: List[int], target:int)-> int:

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return left


if __name__ == "__main__":

    nums = [1, 3, 5, 6]
    print(searchInsert(nums=nums, target=7 ))
