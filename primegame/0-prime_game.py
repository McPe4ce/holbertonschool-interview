#!/usr/bin/python3

def isWinner(x, nums):
    if x == 0 or not nums:
        return None

    max_n = max(nums)

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

    for n in nums:
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
