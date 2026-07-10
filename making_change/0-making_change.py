#!/usr/bin/python3
"""Module that determines the fewest number of coins needed to meet
a given amount total.
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a total.

    Args:
        coins (list): List of the values of the coins available.
        total (int): The amount to reach.

    Returns:
        int: The fewest number of coins needed to meet total.
            0 if total is 0 or less.
            -1 if total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # min_coins[i] = fewest coins to make amount i
    min_coins = [0] + [float('inf')] * total

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount and min_coins[amount - coin] + 1 < min_coins[amount]:
                min_coins[amount] = min_coins[amount - coin] + 1

    return min_coins[total] if min_coins[total] != float('inf') else -1


