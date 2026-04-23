
def longestSum(arr : List[int], k: int)->int:
    left, right, curr_sum, best = 0, 0, 0, 0

    while right < len(arr):
        curr_sum += arr[right]

        while curr_sum > k:
            curr_sum -= arr[left]
            left += 1

        best = max(best, right -left +1)

    return best


if __name__ == '__main__':
    arr = [2, 1, 5, 1, 3, 2, 1, 4]
    k = 7

    print(longestSum(arr, 7))
