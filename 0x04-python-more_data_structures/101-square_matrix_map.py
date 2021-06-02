#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda line: (list(map(lambda k: k*k, line))), matrix))
