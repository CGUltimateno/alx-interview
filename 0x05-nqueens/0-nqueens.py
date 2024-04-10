#!/usr/bin/python3
"""N queens puzzle"""
import sys


def is_safe(board, row, col):
    """
  Checks if a queen can be placed at the given row and column without attacking other queens.
  """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def solve_n_queens(board, col):
    """
  Solves the N-queens problem using backtracking.
  """
    if col >= len(board):
        for row in board:
            print("".join(['Q' if x == 1 else '.' for x in row]))
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_n_queens(board, col + 1)
            board[i][col] = 0
