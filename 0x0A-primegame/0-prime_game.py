#!/usr/bin/python3
"""Prime Game."""


def is_prime(n):
    """Check if a number is prime."""
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos


def prime_game(n, m):
    """Determine who wins the game."""
    if n is None or m is None or n == 0 or m == []:
        return None
    Maria = Ben = 0
    for i in range(n):
        primeNos = is_prime(m[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
