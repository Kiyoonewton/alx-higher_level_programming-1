#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = []
    for k in matrix:
        my_matrix.append([number ** 2 for number in k])
    return my_matrix
