#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = [[m ** 2 for m in row] for row in matrix]
    return my_matrix
