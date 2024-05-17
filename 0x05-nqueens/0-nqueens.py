#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at position (row, col) on the board
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N: int) -> None:
    """Solve N-Queens problem with backtracking algorithm"""
    def backtrack(board: list[int], row: int) -> None:
        """
        Recursively try all possible positions of a queen on the current row
        """
        if row == N:
            print_solution(board)
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1

    def print_solution(board: list[int]) -> None:
        """Print the solution to the N-Queens problem"""
        solution = [(i, board[i]) for i in range(N)]
        print(solution)

    board = [-1] * N
    backtrack(board, 0)


def main():
    """
    Entry point of the program.

    The program takes one command line argument, N, the number of queens.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
