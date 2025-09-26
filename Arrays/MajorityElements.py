from typing import List

def majority_elements(nums: List[int])->int:

    """
    majority_elements is element which appears more than n/2 times
    n = [ 3, 2, 3]
    a = [2, 2, 1, 1, 1, 2, 2]
    """

    count = {}
    res , max_count = 0 , 0

    for n in nums:
        count[n] = 1 + count.get(n, 0)
        res = n if count[n] > max_count else res
        max_count = max(count[n], max_count)

    return res


if __name__ == '__main__':
    a = [2, 2, 1, 1, 1, 2, 2]

    print(majority_elements(a))
