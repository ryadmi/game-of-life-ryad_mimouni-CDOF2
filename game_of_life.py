# -*- coding: utf-8 -*-

# game_of_life.py


import random
import time
import os

def initialize_board(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_board(board):
    for row in board:
        print(' '.join(['#' if cell else ' ' for cell in row]))

def update_board(board):
    new_board = [[0] * len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            live_neighbors = sum(board[x][y] for x in range(i-1, i+2) for y in range(j-1, j+2)
                                if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x != i or y != j))
            new_board[i][j] = (live_neighbors == 3) or (live_neighbors == 2 and board[i][j])
    return new_board

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def game_of_life(rows, cols, generations):
    board = initialize_board(rows, cols)
    for _ in range(generations):
        clear_screen()
        print_board(board)
        board = update_board(board)
        time.sleep(0.5)

if __name__ == "__main__":
    game_of_life(20, 40, 50)
