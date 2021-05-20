#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    matrix must be a list of lists of integers or floats
    otherwise raise a TypeError exception with the message
    'matrix must be a matrix (list of lists) of integers/floats'

    Each row of the matrix must be of the same size
    otherwise raise a TypeError exception with the message
    'Each row of the matrix must have the same size'

    div must be a number (integer or float)
    otherwise raise a TypeError exception with the message
    'div must be a number'

    div can’t be equal to 0
    otherwise raise a ZeroDivisionError exception with the message
    'division by zero'

    All elements of the matrix should be divided by div,
    rounded to 2 decimal places

    Returns a new matrix
    """

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        for num in row:
            if type(num) is not int:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    len_not_row = len(matrix[0])
    for row in matrix:
        if len(row) != len_not_row:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = matrix.copy()

    if type(div) is not int:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in range(len(new_matrix)):
        for column in range(len(new_matrix[row])):
            new_matrix[row][column] = \
                round(float(new_matrix[row][column] / div), 2)

    return new_matrix
