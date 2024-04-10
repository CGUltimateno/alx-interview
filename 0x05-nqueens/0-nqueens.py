#!/usr/bin/python3
"""N queens puzzle"""
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    N = sys.argv[1]
    try:
        N = int(N)
        if N < 4:
            print("N must be at least 4")
            exit(1)
    except ValueError:
        print("N must be a number")
        exit(1)
