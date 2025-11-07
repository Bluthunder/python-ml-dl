from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    merged = []
    i = j = 0

    # Merge both arrays
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Add remaining elements
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    # Find median
    n = len(merged)
    mid = n // 2

    if n % 2 == 1:
        return float(merged[mid])
    else:
        return (merged[mid - 1] + merged[mid]) / 2.0

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))
