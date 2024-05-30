#!/usr/bin/python3
"""0-rorate_2d_matrix - Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    :param matrix: A 2D matrix of integers representing the input matrix.
    :type matrix: List[List[int]]
    :return: None
    """
    num = len(matrix)
    for layer in range(num // 2):
        start, end, offset = layer, num - 1 - layer, 0
        for i in range(start, end):
            top = matrix[start][i]
            matrix[start][i] = matrix[end - offset][start]
            matrix[end - offset][start] = matrix[end][end - offset]
            matrix[end][end - offset] = matrix[i][end]
            matrix[i][end] = top
            offset += 1
