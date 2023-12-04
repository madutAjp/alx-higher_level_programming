#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in range(len(matrix)):
        for k in range(len(matrix[m])):
            print("{:d}".format(matrix[m][k]), end="")
            if k != (len(matrix[m]) - 1):
                print(" ", end="")
        print("")
