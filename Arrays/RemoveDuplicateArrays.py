from typing import List

def removedupe(arr: List[int])->int :
    seen = set()
    idx = 0

    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[idx] = arr[i]
            idx += 1

    return idx

def remove_duplicates_2Pointer(arr: List[int])-> int:

    if len(arr) == 0:
        return 0

    writePos = 0
    for readPos in range(1, len(arr)):
        if arr[readPos] != arr[writePos]:
            writePos += 1
            arr[writePos] = arr[readPos]

    return writePos + 1

if __name__ == '__main__':

    # arr = [1, 1, 2, 2, 3]

    arr = [0,0,1,1,1,2,2,3,3]

    print(remove_duplicates_2Pointer(arr))
