#!/usr/bin/python3
"""
Module 0-nqueens
"""
import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    n_q = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)

if n_q < 4:
    print('N must be at least 4')
    sys.exit(1)


def solve_nqueens(n: int) -> list[list[tuple[int, int]]]:
    """
    Solve the N-queens problem.

    Args:
    - n: The number of the row to solve.

    Returns:
    - A list of lists of tuples, where each tuple represents the row and
    column of a queen in a solution.
    """
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def attack_queen(square: tuple[int, int], queen: tuple[int, int]) -> bool:
    """Check if a queen attacks another queen

    Args:
    - square: A tuple of two integers representing the square of the queen.
    - queen: A tuple of two integers representing the square of the other
    queen.

    Returns:
    - bool: True if the queen attacks the other queen, False otherwise.
    """
    row1, col1 = square
    row2, col2 = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr: tuple[int, int], queens: list[tuple[int, int]]) -> bool:
    """Check if a queen is safe from other queens

    Args:
    - sqr: A tuple of two integers representing the square of the queen.
    - queens: A list of tuples of two integers representing the squares of
    the other queens.

    Returns:
    - bool: True if the queen is safe from other queens, False otherwise.
    """
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


for answer in reversed(solve_nqueens(n_q)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
