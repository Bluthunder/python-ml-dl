from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:

    left = binary(nums, target, True)
    right = binary(nums, target, False)

    return[left, right]

    def binary(nums: List[int], target:int, leftBias:bool)->int:

        l, r = 0, len(nums) - 1
        i = -1

        while l < r:
            m = (l+r)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1

        return i


def first_last_position(nums: List[int], target: int)-> List[int]:
    left, right = 0 , len(nums) - 1

    start, end = -1, -1

    while left <= right :
        mid = left + (right-left)//2

        # print(f'middle element - {nums[mid]}')

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

        else:
            start = mid
            end = mid

            while start - 1 >= 0 and nums[start-1] == target:
                start -= 1

            while end + 1 <= len(nums) and nums[end+1] == target:
                end += 1
            return [start, end]

    return [start, end]




if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8

    # print(searchRange(nums, target))

    print(first_last_position(nums, target))
