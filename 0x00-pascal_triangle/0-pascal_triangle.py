#!/usr/bin/python3
"""
Pascal's Triangle
"""
def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    triangle = pascal_triangle(n - 1)
    last_row = triangle[-1]
    next_row = [1]

    for i in range(len(last_row) - 1):
        next_row.append(last_row[i] + last_row[i + 1])

    next_row.append(1)
    triangle.append(next_row)
    return triangle