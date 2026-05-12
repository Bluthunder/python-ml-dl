
from typing import List, Dict

# This is BRUTE FORCE solution which uses recursion. Time complexity - Big O (S^n), S is length of amount and n in number of coins
# Space complexity is Big O(S) due to recursion stack
def coin_change(coins: List[int], amount: int)->int:

    if amount < 0:
        return -1

    if amount == 0:
        return 0

    min_coin = float('inf')

    for coin in coins:
        result = coin_change(coins, amount-coin)

        if result >= 0 and result < min_coin:
            min_coin = result + 1

    return - 1 if min_coin == float('inf') else min_coin


# This is opmitzed with top down memoization, T
def coin_change_optimized_memo(coins: List[int], amount: int)->int:

    memo = {}

    return coin_change_helper(coins, amount, memo)


def coin_change_helper(coins: List[int], rem: int, memo: Dict):

    if rem < 0:
        return -1

    if rem == 0:
        return 0

    min_coins = float('inf')

    for coin in coins:
        result = coin_change_helper(coins, rem-coin, memo)

        if result >= 0 and result < min_coins:
            min_coins = result + 1

    memo[rem] = -1 if min_coins == float('inf') else min_coins

    return memo[rem]


# This is bottom up tabulation
def coin_change_optimized_tabulation(coins: List[int], amount: int)->int:
    dp = [amount + 1] * (amount+1)

    dp[0]=0

    for i in range(1, amount+1):
        for coin in coins:
            if coin <=i:
                dp[i] = min(dp[i], dp[i-coin]+1)

    return -1 if dp[amount] > amount  else dp[amount]


if __name__ == '__main__':

    coins = [1, 2, 5]
    amount = 11

    print(coin_change(coins, amount))

    print(coin_change_optimized_memo(coins, amount))
