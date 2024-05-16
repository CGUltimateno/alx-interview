#!/usr/bin/python3
"""Prime Game."""

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_game(n, m):
    """Determine who wins the game."""
    if n == 0 or n == 1:
        return None
    if m == 0:
        return None
    if n == 2:
        return "Ben"
    if n == 3:
        return "Maria"
    if m == 1:
        return "Maria"
    ben = 0
    maria = 0
    for i in range(n, m + 1):
        if is_prime(i):
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
