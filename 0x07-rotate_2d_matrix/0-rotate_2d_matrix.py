#!/usr/bin/python3
"""Rotating 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Function to rotate a 2d matrix"""
    matrix_len = len(matrix)

    for i in range(matrix_len):
        """transposing the matrix"""
        for j in range(i, matrix_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    """reverse the matrix"""
    for i in range(matrix_len):
        matrix[i].reverse()
