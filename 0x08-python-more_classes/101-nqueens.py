#!/usr/bin/python3
'''Task 11 module'''


import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)
Q = int(sys.argv[1])

'''chessboard'''
'''matrix with all elements 0'''
board = [[0] * Q for _ in range(Q)]


def is_attack(i, j):
    '''checking if there is a queen in row or column'''
    for k in range(0, Q):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    '''checks diagonals'''
    for k in range(0, Q):
        for l in range(0, Q):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False


def N_queen(n):
    '''if n is 0, solution found'''
    if n == 0:
        return True
    for i in range(0, Q):
        for j in range(0, Q):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(is_attack(i, j))) and (board[i][j] != 1):
                board[i][j] = 1
                if N_queen(n - 1):
                    return True
                board[i][j] = 0
    return False

N_queen(Q)
for i in board:
    print(i)
