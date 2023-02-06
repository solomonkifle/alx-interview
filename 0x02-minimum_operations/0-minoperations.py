#!/usr/bin/python3
"""calculates the fewest number of operations needed to result
in exactly n H characters in the file"""
import math


def factors(n):
    """get factors"""
    base = int(math.sqrt(n))
    factors = {}
    for i in range(2, base + 1):
        repeat = 1
        while n % i == 0:
            factors["{}".format(i)] = repeat
            n = int(n / i)
            repeat += 1
    if n != 1:
        factors["{}".format(n)] = 1
    return factors


def minOperations(n):
    """get min operations"""
    f = factors(n)
    operations = 0
    for k, v in f.items():
        operations += int(k)
        if v > 1:
            operations += v
    return operations
