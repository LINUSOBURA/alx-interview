#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins to ensure we process smaller coins first
    coins.sort()

    # Initialize dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Process each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
