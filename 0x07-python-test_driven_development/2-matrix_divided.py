#!/usr/bin/python3
"""
   Function to divide a matrix
   by the same variable
"""


def matrix_divided(matrix, div):
    """matrix_divided"""
    length = 0
    new_matrix = []
    mssg1 = "matrix must be a matrix (list of lists) of integers/floats"
    mssg2 = "Each row of the matrix must have the same size"

    if type(matrix) is not list:
        raise TypeError(mssg1)
    for item in matrix:
        if type(item) is not list:
            raise TypeError(mssg1)
        for i in item:
            if type(i) is not int and type(i) is not float:
                raise TypeError(mssg1)
        length = len(matrix[0])
        if len(item) != length:
            raise TypeError(mssg2)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for item in matrix:
            submatrix = []
            for x in item:
                submatrix.append(round(float(x / div), 2))
            new_matrix.append(submatrix)
    return new_matrix
