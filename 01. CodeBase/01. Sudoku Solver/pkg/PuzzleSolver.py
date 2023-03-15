# this library will print the puzzle
import DisplayTurtle as disp



def solve_sudoku(sudoku):
    '''
        Calls the required supporting functions
    '''

    # initializing turtle Pen for display
    myPen = disp.initialize_turtle()

    # this will draw the lines of the grid
    disp.drawGrid(myPen)

    # this will print the numbers of the puzzle
    disp.print_digits(sudoku, myPen)

    # accessing the solution of the puzzle
    isSudokuSolved = solve(sudoku, myPen)

    # handling the unsolvalbe puzzle
    if not isSudokuSolved:
        print("Puzzle is unsolvalble.")    



def solve(puzzle, myPen):
    """
        Solves a Sudoku puzzle using backtracking.
    """
    # Find the next empty cell
    row, col = find_empty_cell(puzzle)

    # If there are no more empty cells, the puzzle is solved
    if row is None:
        return True

    # Try each possible value for the empty cell
    for num in range(1, 10):
        if is_valid_move(puzzle, row, col, num):
            puzzle[row][col] = num

            # Recursively try to solve the puzzle with the new value
            if solve(puzzle, myPen):
                disp.print_single_digit(num, row, col, myPen)
                return True

            # If the recursive call did not solve the puzzle, backtrack and try again
            puzzle[row][col] = 0

    # If no value works, the puzzle cannot be solved
    return False



def find_empty_cell(puzzle):
    """
        Finds the next empty cell in the puzzle.
    """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col

    # If there are no empty cells, return None
    return None, None



def is_valid_move(puzzle, row, col, num):
    """
        Determines whether a move is valid by checking the row, column, and 3x3 subgrid.
    """
    # Check row
    if num in puzzle[row]:
        return False

    # Check column
    if num in [puzzle[i][col] for i in range(9)]:
        return False

    # Check 3x3 subgrid
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if puzzle[i][j] == num:
                return False

    # If the move passes all checks, it is valid
    return True



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