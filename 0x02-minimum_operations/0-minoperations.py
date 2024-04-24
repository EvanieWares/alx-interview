#!/usr/bin/python3
"""
Module 0-minoperations

A module that demonstrates a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    n H characters in the file.

    Parameters:
    - n (int): The number of characters

    Returns:
    - The fewest number of operations
    """
    for i in range(2, n + 1):
        if n % i == 0:
            return i + minOperations(int(n / i))
    return 0
