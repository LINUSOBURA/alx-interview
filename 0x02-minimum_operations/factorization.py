#!/usr/bin/env python3
import math


def get_prime_fators(n):
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


Factors = get_prime_fators(5)
print(Factors)
