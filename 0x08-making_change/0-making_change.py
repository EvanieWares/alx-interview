#!/usr/bin/python3
"""
Module 0-making_change

Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    A function that calculates the fewest number of coins needed to meet
    a given total amount.

    Parameters:
    - coins: a list of integers representing the different values of coins
    available
    - total: an integer representing the target total amount

    Returns:
    - An integer representing the fewest number of coins needed to meet the
    total amount, or -1 if it's not possible to form the total
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
