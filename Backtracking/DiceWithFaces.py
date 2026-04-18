
from typing import List

def dice_combination(n: int, m: int)->List[int]:

    result = []

    def backtrack(path):
        if len(path) == n:
            result.append(path[:])
            return

        for i in range(1, m+1):
            path.append(i)
            backtrack(path)
            path.pop()

    backtrack([])
    return result



if __name__ == '__main__':
    n = 2
    m = 3

    print(dice_combination(n, m))

    
