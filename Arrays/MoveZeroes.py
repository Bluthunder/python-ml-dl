"""

i/p arr = [1, 0, 3, 4, 0]

o/p arr = [1, 3, 4, 0, 0]

"""

from typing import List


# NAIVE METHOD WITHOUT ANY OPTIMIZATION
def move_zeroes(arr:List)->List:
    n = len(arr)
    results = [0] * n

    j = 0

    for i in range(n):
        if arr[i] != 0:
            results[j] = arr[i]
            j += 1

    for k in range(j, n):
        results[k] = 0

    for i in range(n):
        arr[i] = results[i]

    return arr


# This does not use an extra array
def move_zeroes_optimization(arr: List)->List:
    n = len(arr)

    writePos = 0

    for i in range(n):
        if arr[i] != 0:
            arr[writePos] = arr[i]
            writePos += 1

    while writePos < n :
        arr[writePos] = 0
        writePos += 1

    return arr


def move_zeroes_further_optimized(arr: List)->List:
    n = len(arr)

    writePos = 0

    for readPos in range(n):
        if arr[readPos] != 0:
            if readPos != writePos:
                arr[readPos], arr[writePos] = arr[writePos], arr[readPos]
            writePos += 1

    return arr



if __name__ == '__main__':

    arr = [1, 0, 3, 4, 0]

    print(f'Naive Method - {move_zeroes(arr)}')

    print(f'Without extra array - {move_zeroes_optimization(arr)}')


    print(f'Inplace Swap - {move_zeroes_further_optimized(arr)}')
