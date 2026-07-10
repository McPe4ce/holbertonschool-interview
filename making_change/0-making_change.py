#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # min_coins[i] = fewest coins to make amount i
    min_coins = [0] + [float('inf')] * total

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount and min_coins[amount - coin] + 1 < min_coins[amount]:
                min_coins[amount] = min_coins[amount - coin] + 1

    return min_coins[total] if min_coins[total] != float('inf') else -1


