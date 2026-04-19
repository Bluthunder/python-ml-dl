
from typing import List

def powerset_iterative(nums: List[int])->List[List[int]]:

    result = [[]]

    for num in nums:
        result += [subset + [num] for subset in result]

    return result


def powerset_backtrack(nums: List[int])->List[List[int]]:
    result = []

    def backtrack(start: int, current: List[int])->None:
        result.append(current[:])

        for i in range(start, len(nums)):
            current.append(nums[i])   # Choose
            backtrack(i+1, current)  # Explore
            current.pop()    # Unchoose

    backtrack(0, [])
    return result




if __name__ == '__main__':
    nums = [1, 2, 3]

    print(powerset_iterative(nums))
    print(powerset_backtrack(nums))
