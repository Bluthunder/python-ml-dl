from typing import List


# This uses an extra array so space complexity is O(m+n)
def merge(nums1: List, m:int, nums2: List, n:int)->None:

    p1, p2 , p = 0, 0, 0

    sorted_arr = [0] * (m+n)

    while p1 < m and p2 < n:
        if nums1[p1] <= nums2[p2]:
            sorted_arr[p] = nums1[p1]
            p1 += 1
        else:
            sorted_arr[p] = nums2[p2]
            p2 += 1

        p += 1


    while p1 < m:
        sorted_arr[p] = nums1[p1]
        p1 += 1
        p += 1

    while p2 < n:
        sorted_arr[p] = nums2[p2]
        p2 += 1
        p += 1

    nums1[:m+n] = sorted_arr



def merge_optimized(nums1: List[int], m:int, nums2: List[int], n:int)->None:
    p1, p2, p = m-1, n-1, m+n-1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1

        p -= 1

    while p2 >= 0:
        nums1[p] = nums2[p2]
        p -= 1
        p2 -= 1





if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    merge_optimized(nums1, m, nums2, n)

    print(nums1)
