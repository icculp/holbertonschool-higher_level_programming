#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix[0]):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (j + 1 == len(matrix[i])):
                    print("{:d}".format(matrix[i][j]))
                else:
                    print("{:d} ".format(matrix[i][j]), end="")
    else:
        print()
