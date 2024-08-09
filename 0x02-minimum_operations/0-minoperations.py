#!/usr/bin/env python3

"""
A python script to solve the "H" file manipulation challenge!
"""

def minOperations(n)
    """
    A method that calculates the fewest number of operations needed to result
    in exactly n H characters in a file
    """
    if n == 1:
        return 0  # No operations needed for one "H"

    operations = 0
    current = 1
    clipboard = ""

    while current < n:
        if n % current == 0:
            clipboard = "H" * current  # Copy All
            operations += 1
        current += len(clipboard)  # Paste
        operations += 1

    return operations if current == n else 0
