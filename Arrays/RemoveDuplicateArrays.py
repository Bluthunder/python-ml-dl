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



if __name__ == '__main__':

    arr = [1, 1, 2, 2, 3]
    print(removedupe(arr))


    
