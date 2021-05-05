#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for coln in ligne:
            print("{:d}".format(coln), end=" " if coln != ligne[-1] else "")
        print()
