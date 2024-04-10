#!/usr/bin/python3
"""N queens puzzle"""
import sys


def is_safe(board, row, col):
    """n queen """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    X = int(sys.argv[1])
    try:
        if X < 4:
            print("N must be at least 4")
            exit(1)
    except ValueError:
        print("N must be a number")
        exit(1)


if __name__ == '__main__':
    is_safe()
