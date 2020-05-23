#!/usr/bin/python3
'''2-matrix_divided docstring'''


def matrix_divided(matrix, div):
    '''Divides a matrix'''
    if not all(isinstance(li, list) for li in matrix):
        raise TypeError("matrix must be a matrix (li"
                        "st of lists) of integers/floats")
    for li in matrix:
        for x in li:
            if type(x) not in [int, float]:
                raise TypeError("matrix must be a matrix (li"
                                "st of lists) of integers/floats")
    for li in matrix:
        if len(li) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matr = [[None] * len(matrix[0]) for x in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matr[row][col] = float("{:.2f}".format((matrix[row][col] / div)))
    return matr
