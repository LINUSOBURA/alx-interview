#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize the dp array with a value larger than the maximum possible number of coins needed
    dp = [float('inf')] * (total + 1)

    # Base case: zero coins are needed to make the total of 0
    dp[0] = 0

    # Iterate over each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met with the given coins
    return dp[total] if dp[total] != float('inf') else -1
