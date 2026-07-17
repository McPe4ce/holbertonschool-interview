#!/usr/bin/python3
"""Module for solving the Prime Game."""


def isWinner(x, nums):
    """Determine who wins the most rounds of the prime game.

    Maria and Ben alternate turns removing a prime number and all
    its multiples from the set {1, ..., n}. The player unable to
    move loses. The winner of a round is determined by the parity
    of the count of primes <= n: a prime can only be removed by
    being explicitly picked, so the number of turns in a round
    always equals that count. An odd count means Maria (who moves
    first) makes the last move, so she wins; an even count means
    Ben wins.

    Args:
        x (int): the number of rounds played.
        nums (list): the value of n for each round; only the first
            x elements are used.

    Returns:
        str: "Maria" or "Ben" if one won more rounds, else None.
    """
    if x == 0 or not nums:
        return None

    rounds = nums[:x]
    max_n = max(rounds)

    is_prime = [True] * (max_n + 1)
    is_prime[0] = False
    if max_n >= 1:
        is_prime[1] = False
    for p in range(2, int(max_n ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, max_n + 1, p):
                is_prime[multiple] = False

    primes_up_to = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        primes_up_to[i] = primes_up_to[i - 1] + (1 if is_prime[i] else 0)

    maria = 0
    ben = 0

    for n in rounds:
        prime_count = primes_up_to[n]
        if prime_count % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
