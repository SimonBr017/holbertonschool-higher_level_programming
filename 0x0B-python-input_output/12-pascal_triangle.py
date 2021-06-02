#!/usr/bin/python3
"""function pascal triangle"""


def pascal_triangle(n):
    """return a list of lists of integers
    representing the Pascal’s triangle of n"""
    pascal = [[1]]
    if n <= 0:
        return []
    for row in range(1, n):
        pascal.append([1])
        for conter in range(row):
            try:
                new = pascal[row - 1][conter + 1] + pascal[row - 1][conter]
            except:
                new = 1
            if row - 1 == conter:
                new = 1
            pascal[row].append(new)
    return pascal
