#!/usr/bin/python3
"""Define a matrix"""


def matrix_divided(matrix, div):
    """Represent a matrix.

    Args:
        Matrix: a list of int or float
        div: a number that will divide this list

    Returns:
        A new matrix with results divided

    Raises:
        TypeError: if matix is not a list of int or floats
        TypeError: if any row in matrix is not same size
        TypeError: if div is not an int
        ZeroDivisionError: if div is equal to 0
        """
    if not all (isinstance(row, list) \
            for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not all(isinstance(elements, (int, float))\ for row in matrix for element in row):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not all(len(row) == len(matrix[0])\ for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
