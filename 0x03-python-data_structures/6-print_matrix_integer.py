#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for column in ligne:
            print("{:d}".format(column), end=" " if column != ligne[-1] else "")
        print()
