"""
Solves the N-Queens problem using backtracking.

The N-Queens problem is the problem of placing N chess queens on an NxN
chessboard such that none of the queens attack each other. A queen attacks
if it is in the same row, column, or diagonal as another queen.

The algorithm implemented here uses backtracking to find all possible
solutions to the N-Queens problem. It starts by placing a queen in the
first column of the first row. It then recursively tries to place the
remaining N-1 queens in the remaining columns and rows. If it is not
possible to place a queen in a given column and row, it backtracks and
tries another column and row.

The function nqueens takes an integer N as input and returns a list of
lists, where each sublist is a solution to the N-Queens problem and
contains the positions of the N queens in the format (row, column).

Example:
    >>> nqueens(4)
    [[(0, 0), (1, 2), (2, 1), (3, 3)], [(0, 1), (1, 3), (2, 0), (3, 2)]]
"""
