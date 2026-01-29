from typing import List


# This is Brute force solution, time complexity is O(N^2)
def max_area_bf(height: List[int])->int:

    maxArea = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = min(height[i], height[j]) * (j-i)
            maxArea = max(maxArea, area)

    return maxArea



# This is optimized for time complexity, time complexity is O(N)
def max_area_optimised(height: List[int])-> int:
    maxArea = 0

    left = 0
    right = len(height) - 1

    while left < right:
        area = min(height[left], height[right]) * (right-left)

        maxArea = max(area, maxArea)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxArea


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]

    print(max_area_bf(height))

    print(max_area_optimised(height))
