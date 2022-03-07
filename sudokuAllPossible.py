'''0 means the cells where no value is assigned'''
""" This module prints all the possible solutions of a Sudoku puzzle

idea link - https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/ 

@author: Anwesha Pradhananga
@date: January 2022
"""

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


more = "y"


def print_board(board):
    """Prints the board of the sudoku as a game"""

    for i in range(0,9):
        if i % 3 == 0:
            print("-------------------------")
            
        for j in range(0,9):
            if j % 3 == 0:
               print("| ", end="")
            print (board[i][j], end=" ")
        print("|")
        
    print("-------------------------")


def valid_move(board, row, col, num):
    """Checks if the move is valid by checking the number in that row, column and square."""
    
    #Check all rows
    for i in range(9):
        if board[i][col] == num:
            return False
    
    #Check all columns
    for j in range(9):
        if board[row][j] == num:
            return False
    
    #Check square
    r = row // 3 * 3
    c = col // 3 * 3
    
    for i in range(3):
        for j in range(3):
            if board[r + i][c + j] == num:
                return False
            
    return True


def solve_game(board):
    """Checks if the board can be solved at that point in the game."""
    
    global more
    
    #Checks if the grid is empty
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                
                for i in range(1,10):
                    if valid_move(board, row, col, i):
                        board[row][col] = i
                        
                        #Recursively tries to solve the board.
                        if not more == "n":
                            solve_game(board)
                        
                        #Assigns that grid to 0 to backtrace the board
                        board[row][col] = 0
                        
                return False
            
    print_board(board)
    more = input("More possible?")
  
  
def main(board):
    """Calls the solve_game function"""
    
    if solve_game(grid):
        pass
    else:
        print("No more possible")


main(grid)