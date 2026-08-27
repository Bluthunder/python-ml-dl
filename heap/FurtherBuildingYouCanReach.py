
from typing import List

def furtherBuildingYouCanReach(heights: List[int], bricks: int, ladders: int)->int:

    def dfs(index, bricks, ladders):
        if index == len(heights) - 1:
            return index

        diff = heights[index+1] - heights[index]

        if diff <= 0:
            return dfs(index+1, bricks, ladders)

        best = index

        if bricks >= diff:
            best = max(best, dfs(index+1, bricks - diff, ladders))

        if ladders > 0:
            best = max(best, dfs(index+1, bricks, ladders - 1))

        return best

    return dfs(0, bricks, ladders)



if __name__ == '__main__':

    heights = [4,2,7,6,9,14,12]
    bricks = 5
    ladders = 1

    print(furtherBuildingYouCanReach(heights, bricks, ladders))
