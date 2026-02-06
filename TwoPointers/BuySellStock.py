from typing import List


def maxProfit(prices: List[int])->int:
    left , right = 0, 1
    maxP = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)
        else:
            left = right

        right += 1

    return maxP


def best_time_to_buy_sell(prices: List[int])->int:
    minPrice = float('inf')
    maxProfit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price

        profit = price - minPrice

        if profit > maxProfit:
            maxProfit = profit

    return maxProfit




if __name__ == '__main__':
    a = [7,1,5,3,6,4]

    print(maxProfit(a))
