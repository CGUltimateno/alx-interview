#!/usr/bin/python3
"""N queens puzzle"""
import sys


def is_safe(board, row, col, n) -> bool:
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col, n) -> bool:
    """Solve the N queens problem"""
    if col == n:
        print([[i, row.index(1)] for i, row in enumerate(board)])
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve(board, col + 1, n) or res
            board[i][col] = 0

    return res


def nqueens(n):
    """Initialize the board and solve the problem"""
    if not n.isdigit():
        print("N must be a number")
        return False
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        return False

    board = [[0] * n for _ in range(n)]
    solutions = []
    solve(board, 0, n)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])