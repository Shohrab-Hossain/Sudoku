import DisplayTurtle as disp


def find_next_box(sudoku):
    for row in range (9):
        for col in range (9):
            if sudoku[row][col] == 0:
                return (row, col)
    
    return False


def isPossible(sudoku, row, col, n):
    # Checking through row
    for i in range(9):
        if sudoku[row][i] == n and row != i:
            return False

    # Checking through column
    for i in range(9):
        if sudoku[i][col] == n and col != i:
            return False

    
    # calculating subgrid number
    subgrid_row_no = row // 3
    subgrid_col_no = col // 3

    # finding the 1st row and column of sub-grid
    row_1 = subgrid_row_no * 3
    col_1 = subgrid_col_no * 3

    # finding the 3rd row and column of sub-grid
    row_3 = row_1 + 3
    col_3 = col_1 + 3

    # Checking through sub-grid
    for i in range(row_1, row_3):
        for j in range(col_1, col_3):
            if sudoku[i][j] == n and (i,j) != (row, col):
                return False

    return True


def solve(sudoku, myPen):
    # finding the next available box
    next_box = find_next_box(sudoku)

    if next_box is False:
        # no next box is available
        return True
    else:
        # next box is available and extracting the row and col of that box
        row, col = next_box

        for n in range(1,10):
            if isPossible(sudoku, row, col, n):
                sudoku[row][col] = n

                if solve(sudoku, myPen):
                    disp.print_single_digit(n, row, col, myPen)
                    return True
                else:
                    sudoku[row][col] = 0
        
        return False



def solve_sudoku(sudoku):
    myPen = disp.initialize_turtle()
    disp.drawGrid(myPen)
    disp.print_digits(sudoku, myPen)

    isSudokuSolved = solve(sudoku, myPen)

    if not isSudokuSolved:
        print("Solution does not exist. Model misread digits.")    



def print_sudoku(sudoku):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("---------------------")

        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")

            if col == 8:
                print(sudoku[row][col])
            else:
                print(str(sudoku[row][col]) + " ", end="")