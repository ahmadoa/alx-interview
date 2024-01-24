#!/usr/bin/python3
"""0. rotate 2d matrix module"""


def rotate_2d_matrix(matrix):
    """rotates a 2d matrix 90 deg clockwise"""
    n = len(matrix)
    temp = matrix[:]
    for y in range(n):
        dx = []
        for x in range(n-1, -1, -1):
            dx.append(matrix[x][y])
        matrix.append(dx)
    for dx in temp:
        matrix.pop(matrix.index(dx))
