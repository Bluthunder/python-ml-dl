
from typing import List

def merge_bruteforce(nums1: List[int], m:int, nums2: List[int], n:int) -> None:

    for i in range(n):
        nums1[m+i] = nums2[i]

    nums1.sort()



def merge_optimal(nums1: List[int], m:int, nums2: List[int], n:int) -> None:

    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    while j >=0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1



if __name__ == '__main__':

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    merge_optimal(nums1, m, nums2, n)
    print(nums1)
