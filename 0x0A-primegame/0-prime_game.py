#!/usr/bin/python3


def isWinner(x, nums):
    """
    The prime game is a game played with two players, Maria and Ben.
    The game is played with a list of numbers, and the players take turns
    removing prime numbers from the list. The last player who made a move
    is the winner.
    """

    def sieve_of_eratosthenes(n):
        """
			The Sieve of Eratosthenes algorithm to find all prime numbers up to n.
			"""
        primes = []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, n + 1):
            if sieve[i]:
                primes.append(i)
                for multiple in range(i * i, n + 1, i):
                    sieve[multiple] = False
        return primes

    def play_game(n):
        """
			Play the prime game.

			The game is played with two players, Maria and Ben. The game is played
			with a list of numbers, and the players take turns removing prime numbers
			from the list. The last player who made a move is the winner.
			"""
        primes = sieve_of_eratosthenes(n)
        remaining_numbers = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben

        while primes:
            prime = primes.pop(0)
            if prime in remaining_numbers:
                multiples = {prime * k for k in range(1, n // prime + 1)}
                remaining_numbers -= multiples
            if not remaining_numbers.intersection(primes):
                break
            turn = 1 - turn

        return 1 - turn  # The winner is the last one who made a move

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            winner = play_game(n)
            if winner == 0:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
