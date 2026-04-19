
from typing import List

def daily_temperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = [] # pair: [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = (i - stackInd)
        stack.append([t, i])

    return res




if __name__ == '__main__':
    temp = [73, 74, 75, 71, 69, 72, 76, 73]

    print(daily_temperatures(temp))
