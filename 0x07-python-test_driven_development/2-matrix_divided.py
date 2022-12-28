#!/usr/bin/python3
"""
Module 2-matrix_divided definition

"""
def matrix_divided(matrix, div):
    """
    matrix_divided definition

    Args:
        matrix (_type_): list of matrix
        div (_type_): divisor
    """
    if type(matrix) is not int or type(matrix) is not float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not len(matrix[0]) == len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    elif type(div) is not int or type(matrix) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = []
        for i in matrix:
            result = round(i / div, 2)
            new_matrix.append(result)
        return new_matrix
