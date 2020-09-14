"""
File: sudoku.py
Author: @gagank02
Description: 
    A program that generates a new, random sudoku puzzle and then solves it. 
    Or, if wanted, can solve a pre-existing array (such as the commented out 'board' array) using only the solve() function.
"""

from random import randint, shuffle


"""
board = [
    [0, 5, 0, 6, 0, 0, 2, 0, 0],
    [0, 8, 0, 2, 0, 7, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 5, 3, 0],
    [0, 7, 0, 0, 6, 0, 0, 0, 2],
    [0, 0, 0, 9, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 4, 0],
    [0, 0, 5, 0, 0, 0, 6, 0, 3],
    [0, 9, 0, 4, 0, 0, 0, 7, 0],
    [0, 0, 6, 0, 0, 5, 4, 0, 0]
]
"""
# Array representing a completely empty sudoku puzzle
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

numbers = [1, 2 ,3 ,4, 5, 6, 7, 8, 9] # Only possible numbers that can be used in a sudoku puzzle

def print_board(board): # Prints sudoku board
    for i in range(len(board)):
        if i % 3 == 0:
            print("======================")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end = "")    
            if j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ", end = "")
    print("======================")


def generate_full_board(board): # Creates a new, completed/full sudoku puzzle
    if is_full(board): # If the board is full, stops generating numbers to fill the board
        return True
    else: # Finds the coordinates of the next empty square
        y, x = is_empty(board)
    
    shuffle(numbers)
    for num in numbers: # Attempts to put a number 1-9 into a square
        if valid(board, num, (y, x)):
            board[y][x] = num
            
            if generate_full_board(board):
                return True
            
            board[y][x] = 0

    return False


def solve(board):
    pos = is_empty(board) # Finds the coordinates of the next empty square
    if not pos: # If no more empty spaces, stops trying to solve --> puzzle is completed
        return True
    else: # Sets the coordinates of the next empty square
        y, x = pos
    
    for i in range(1,10): # Attempts to put a number 1-9 into a square
        if valid(board, i, (y, x)):
            board[y][x] = i
            
            if solve(board):
                return True
            
            board[y][x] = 0
    
    return False


def is_empty(board): # Returns coordinates of the next square that is empty or contains a '0'
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    
    return None


def is_full(board): # Determines if the board is full
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return False
    
    return True


def valid(board, num, pos): # Determines whether or not a number already exists in a square
    # Checks row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Checks column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Checks 3x3 square section/box
    x_box_pos = pos[1] // 3 # col
    y_box_pos = pos[0] // 3 # row

    for i in range(y_box_pos * 3, y_box_pos * 3 + 3):
        for j in range(x_box_pos * 3, x_box_pos * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True



# Prints empty board --> completed board/answer key
print_board(board)
print("                      ")

generate_full_board(board)
print_board(board)
print("                      ")

# Generates new puzzle based on completed board with a random number of clues
clues = 81 - randint(17,81) # A proper sudoku will have AT LEAST 17 clues, so this will randomly select the number of clues between 17-80
for i in range (1,clues):
    y = randint(0,8)
    x = randint(0,8)
    while board[y][x] == 0:
        y = randint(0,8)
        x = randint(0,8)
    
    board[y][x] = 0


# Prints newly generated puzzle --> solved board/solution
print_board(board)
print("                      ")

solve(board)
print_board(board)
