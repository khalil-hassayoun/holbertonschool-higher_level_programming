#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    string = ''
    for row in matrix:
        string += "\n"
        for item in row:
            string += "{:d} ".format(item)
        string = string[:-1]
    print(string[1:])
