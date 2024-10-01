#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None

    marias_wins = bens_wins = 0

    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = False

    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, max_num + 1, i):
            primes[j - 1] = False

    for _, num in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: num])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
