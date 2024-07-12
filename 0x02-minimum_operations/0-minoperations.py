#!/usr/bin/python3
"""
Minimum operations
"""

import math


def get_prime_fators(n):
    """
    Returns the prime factors of a given number.

    Parameters:
        n (int): The number to find the prime factors of.

    Returns:
        list: A list of prime factors of the given number.

    Examples:
        >>> get_prime_fators(12)
        [2, 2, 3]
        >>> get_prime_fators(15)
        [3, 5]
    """
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n) + 1), 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors


def minOperations(n):
    """
    Calculate the minimum number of operations
    needed to reach a given number.

    Parameters:
        n (int): The target number.

    Returns:
        int: The minimum number of operations
        needed to reach the target number.
    """
    if n <= 1:
        return 0
    operations = 0

    factors = get_prime_fators(n)

    for factor in factors:
        operations += factor

    return operations
