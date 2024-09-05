#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.
    Returns the name of the player with the most wins or None if tied.
    """

    def sieve_of_eratosthenes(n):
        """
        The Sieve of Eratosthenes algorithm to find all prime numbers up to n.
        """
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for multiple in range(i * i, n + 1, i):
                    sieve[multiple] = False
        primes = [i for i in range(n + 1) if sieve[i]]
        return primes

    # Precompute primes up to the maximum n in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Precompute the number of primes up to each number in the range
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if i in primes else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
