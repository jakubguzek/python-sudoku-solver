# Auxiliary functions for printing rows, columns and boxes/chunks of an
# array representing a Sudoku board. Were mostly helpful for troubleshooting
def printRow(array, row):
    for i in range(9):
        print(array[row][i], end=' ')
    print()

def printCol(array, col):
    for i in range(9):
        print(array[i][col], end=' ')
    print()

def printChunk(array, row, col):
    row = row - row%3
    col = col - col%3
    for i in range(3):
        for j in range(3):
            print(array[row+i][col+j], end=' ')
        print()

# Print a board in kinda elegant way
def printBoard(array):
    print(' | ' + "--------- | " * 3)
    for j in [0,3,6]:
        for i in range(j,j+3):
            print(' | ', end='')
            print(array[i][0:3], end=' | ')
            print(array[i][3:6], end=' | ')
            print(array[i][6:9], end=' | \n')
        print(' | ' + "--------- | " * 3)

# Functions for checking if number is present in row, column or a box of
# an array representing a Sudoku Board. They are passed to isAllowed function.
def isInRow(array, row, number):
    for i in range(9):
        if (array[row][i] == number):
            return True
    return False

def isInCol(array, col, number):
    for i in range(9):
        if (array[i][col] == number):
            return True
    return False

def isInChunk(array, row, col, number):
    row = row - row%3
    col = col - col%3
    for i in range(3):
        for j in range(3):
            if (array[row+i][col+j] == number):
                return True
    return False

# Check if a number is allowed to be used in the particular location of a board,
# if so return appropriate Boolean value
def isAllowed(array, row, col, number):
    if (isInRow(array, row, number) == True):
        return False
    if (isInCol(array, col, number) == True):
        return False
    if (isInChunk(array, row, col, number) == True):
        return False
    return True

# Find the coordinates of empty location, if there is no empty locations in a
# board, return 'None'
def locateEmpty(array):
    for i in range(9):
        for j in range(9):
            if (array[i][j] == 0):
                return [i,j]
    return None

# Auxiliary function that checks if the board is correctly solved. Some deprecated
# code is here from the time when I tried to get values of boxes/chunks in the board
# in slightly different way. It works for printing
def checkIfValid(array):
    reference = set(list(range(1,10)))
    for i in range(9):
        row = array[i]
        if set(row) != reference:
            return False
    for i in range(9):
        column = [column[i] for column in array]
        if set(column) != reference:
            return False
    for i in [0,3,6]:
        chunk = []
        chunk2 = []
        chunk3 = []
        for j in range(i,i+3):
            chunk = chunk + array[j][0:3]
            chunk2 = chunk2 + array[j][3:6]
            chunk3 = chunk3 + array[j][6:9]
        if ((set(chunk) != reference) or \
            (set(chunk2) != reference) or \
            (set(chunk3) != reference) \
           ):
            return False
    return True

# Actual function that solves the board. It uses the backtracking algorithm, to
# correct mistakes, which will probably happen often, as solving method in itself is
# stupid and basic (it uses the first number that fits the current location, so it
# will always use the smallest number that is allowed in particular moment). One
# change that could be made is coding the function to use the pre-emptive sets and
# 'Occupancy theorem'. However for now I don't know how to implement it with
# backtracking
def solve(array):
    if (locateEmpty(array) == None):
        return True
    location = locateEmpty(array)
    for i in range(1,10):
        if (isAllowed(array, location[0], location[1], i) == True):
            array[location[0]][location[1]] = i
            if (solve(array) == True):
                return True
            else:
                array[location[0]][location[1]] = 0
    return False

def main():
    array = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    array1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    printBoard(array1)
    solve(array1)
    if (checkIfValid(array1) == True):
        printBoard(array1)

main()
