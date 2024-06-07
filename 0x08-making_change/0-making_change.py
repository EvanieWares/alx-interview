#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total

    :param coins: A list of integers representing the different coin values.
    :param total: An integer representing the total amount.
    :return: Fewest number of coins needed to meet total
             Returns -1 if it is not possible to meet the total amount.
    """
    if total <= 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
