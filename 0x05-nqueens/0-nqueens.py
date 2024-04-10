#!/usr/bin/python3
"""N queens puzzle"""
import sys


def is_safe(board, row, col, n):
    """The N queens puzzle is the challenge of placing N
    non-attacking queens on an N×N chessboard.
    Write a program that solves the N queens problem"""
    for i in range(col):
        if board[i] == row or board[i] == row - col + i or board[i] == row + col - i:
            return False
    return True

