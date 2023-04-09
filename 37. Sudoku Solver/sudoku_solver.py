import numpy as np

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

def is_possible(row, column, number):
    #is the number existing  in the given row?
    for i in range(0,9):
        if board[row][i] == number:
            return False

    #is the number existing  in the given column?
    for i in range(0,9):
        if board[i][column] == number: 
            return False

    #is the number existing  in the square/section?
    #0//3 = 0, 0*3 is 1 section/square 
    #3//3 = 1, 1*3 is 2 section/square
    #6//3 = 2, 2*3 is 3 section/square
    section_x = (column // 3 ) * 3 
    section_y = (row // 3 ) * 3

    for i in range(0,3):
        for j in range(0,3):
            if board[section_y + i][section_x + j] == number: 
                return False

    return True                

def solve():
    global board
    for row in range(0,9):
        for column in range(0,9):
            if board[row][column] == ".":
                for number in range(1,10):
                    if is_possible(row, column, number):
                        board[row][column] = number
                        solve()
                        board[row][column] = "."
                return

    print(np.matrix(board))
    input("More Solution")
solve()
