from typing import List


def three_sum(nums: List[int])->List[List[int]]:

    res = []

    # Sort array to better remove duplicates

    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0 :
                k = k -1
            elif total < 0:
                j = j + 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j = j + 1

                while nums[j] == nums[j - 1] and j < k:
                    j = j+1

    return res



if __name__ == '__main__':
    a = [-1,0,1,2,-1,-4]

    print(three_sum(a))
