#!/usr/bin/python3
"""
This module contains a function for creating a pascal triangle
"""


def pascal_triangle(n):
    """
    This function generates a pascals triangle
    """
    if n <= 0:
        return ([])
    triangle = [[1] * i for i in range(1, n+1)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle
