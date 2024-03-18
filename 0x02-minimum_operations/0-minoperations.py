#!/usr/bin/python3
"""
This module contains a function that return
the mimumm number of copy paste operations
"""


def minOperations(n):
    """
    This function calculated the minimum number of copy-paste
    operations needed to obtain n amount of characters.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            n //= factor
            operations += factor
        else:
            factor += 1

    return operations
