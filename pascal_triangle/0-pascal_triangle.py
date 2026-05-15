#!/usr/bin/python3
"""Module that creates the pascal triangle"""


def pascal_triangle(n):
    """Function that initialise the triangle"""
    pascalou = []

    for indexor in range(n):
        row = [1] * (indexor + 1)

        for j in range(1, indexor):
            row[j] = pascalou[indexor-1][j-1] + pascalou[indexor-1][j]

        pascalou.append(row)
    return pascalou
