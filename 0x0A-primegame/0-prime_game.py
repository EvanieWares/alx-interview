#!/usr/bin/python3
"""
Prime Game Module

This module defines a function to determine the winner of a prime number game
played between Maria and Ben.

Game Rules:
- Given a set of consecutive integers starting from 1 up to and including n,
    players take turns choosing a prime number from the set.
- When a prime number is chosen, that number and all its multiples are removed
    from the set.
- The player that cannot make a move loses the game.

Function:
    - isWinner(x, nums)
        Determines the overall winner after x rounds of the game, where each
        round has a different n value.

Examples:
    >>> isWinner(3, [4, 5, 2])
    'Maria'
    >>> isWinner(5, [2, 5, 1, 4, 3])
    'Ben'

Author:
    - Chisomo Psyelera
"""


def sieve_of_eratosthenes(max_n):
    """
    Generate a list of prime numbers up to max_n using the
    Sieve of Eratosthenes algorithm.

    Args:
        max_n (int): The maximum number to check for primes.

    Returns:
        list: A list of prime numbers up to max_n.
    """
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, max_n + 1) if is_prime[p]]
    return prime_numbers


def isWinner(x, nums):
    """
    Determine the winner after x rounds of the game.

    Args:
    - x (int): The number of rounds to be played.
    - nums (list): A list of integers where each integer represents the upper
        bound n for a round.

    Returns:
    str: The name of the player with the most wins ('Maria' or 'Ben'),
    or None if they have an equal number of wins.
    """
    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            if len(sieve_of_eratosthenes(n)) % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
