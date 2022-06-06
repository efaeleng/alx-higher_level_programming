#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for num in list:
            if num != list[0]:
                print(" ", end='')
            print("{:d}".format(num), end='')
        print()
