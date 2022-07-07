#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    columns = len(matrix[0])

    new_matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(matrix[i][j])
        new_matrix.append(row)

    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] = new_matrix[i][j]**2

    return new_matrix
