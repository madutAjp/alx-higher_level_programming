#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[0 for _ in range(len(row))] for row in matrix]
    for m in range(len(matrix)):
        for k in range(len(matrix[m])):
            result[m][k] = matrix[m][k] ** 2
            return result
