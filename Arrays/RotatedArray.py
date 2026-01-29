
from typing import List


# this is with an extra array
def rotated_array(nums: List[int], k: int) -> None:
    n = len(nums)

    k = k % n

    rotated = [0] * n

    for i in range(n):
        rotated[(i+k) % n] = nums[i]


    for i in range(n):
        nums[i] = rotated[i]



# This saves extra space for array
def rotated_optimal(nums: List[int], k: int)-> None:

    n = len(nums)

    k = k % n

    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)


def reverse(arr: List[int], start: int, end: int)->None:

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1




if __name__ == '__main__':
    array = [1,2,3,4,5,6,7]
    k = 3

    # rotated_array(array, k)

    rotated_optimal(array, k)

    print(array)
