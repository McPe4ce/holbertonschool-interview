#!/usr/bin/env python3

def pascal_triangle(n):
    pascalou = []

    for indexor in range(n):
        row = [1] * (indexor + 1)
    
        for dedex in range(1, indexor):
            row[dedex] = pascalou[indexor - 1][dedex - 1] + pascalou[indexor-1][dedex]
    
        pascalou.append(row)
    return pascalou


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
