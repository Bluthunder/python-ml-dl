from typing import List

def peakElement(arr: List[int])->int:
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right)//2

        if arr[mid] > arr[mid+1]:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    arr = [1,2,1,3,5,6,4]
    print(peakElement(arr))
