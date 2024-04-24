#!/usr/bin/python3
"""
Module 0-minoperations

A module that demonstrates a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
"""


def isPrimeNumber(num):
    """
    Checks if a number is a prime number.

    Parameters:
    - num (int): The number to check

    Returns:
    - True if the number is a prime number
    - False if the number is not a prime number
    """
    for i in range(2, round(num / 2)):
        if num % i == 0:
            return False
    return True


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
        if isPrimeNumber(i) and n % i == 0:
            return i + minOperations(int(n / i))
    return 0

print(minOperations(1))
