# !pip install ColabTurtlePlus
from ColabTurtlePlus import Turtle



config = {
    'topLeft_x' : -170,
    'topLeft_y' : 170,
    'intDim' : 38
}



def initialize_turtle():
    '''
        This function initializes the Turtle Environment.
    '''

    # initialize turtle
    Turtle.clearscreen()
    Turtle.setup(460,460)

    # initialize pen to draw
    myPen = Turtle.Turtle()
    
    # initialize pen parameter
    myPen.speed(13)
    myPen.color("#000000")
    myPen.hideturtle()
    
    return myPen



def digit(digit, x, y, style, myPen):
    '''
        This function prints a digit inside a box.
    '''

    # defining font style
    font = ('Arial', 18, style)
    
    # setting up the pen
    myPen.penup()
    myPen.goto(x,y)    		  
    
    # writing the digit
    myPen.write(
        digit, 
        align = "center", 
        font = font
    )



def drawGrid(myPen): 
    '''
        This function draws a 9x9 grid.
    '''

    topLeft_x = config['topLeft_x']
    topLeft_y = config['topLeft_y']
    intDim = config['intDim']

    for row in range(0,10):
        if (row % 3) == 0:
            myPen.pensize(3)
        else:
            myPen.pensize(1)
        myPen.penup()
        myPen.goto(topLeft_x, topLeft_y-row*intDim)
        myPen.pendown()
        myPen.goto(topLeft_x+9*intDim, topLeft_y-row*intDim)
    
    for col in range(0,10):
        if (col % 3) == 0:
            myPen.pensize(3)
        else:
            myPen.pensize(1)    
        myPen.penup()
        myPen.goto(topLeft_x+col*intDim, topLeft_y)
        myPen.pendown()
        myPen.goto(topLeft_x+col*intDim, topLeft_y-9*intDim)



def print_digits(grid, myPen): 
    '''
        This function prints all the digits of a sudoku.
    '''

    topLeft_x = config['topLeft_x']
    topLeft_y = config['topLeft_y']
    intDim = config['intDim']

    for row in range (9):
        for col in range (9):
            if grid[row][col] != 0:
                digit(
                    digit = grid[row][col],
                    x = topLeft_x+col*intDim+18,
                    y = topLeft_y-row*intDim-intDim+12,
                    style = 'bold',
                    myPen = myPen
                )



def print_single_digit(n, row, col, myPen):
    '''
        This function prints a single digit.
    '''

    topLeft_x = config['topLeft_x']
    topLeft_y = config['topLeft_y']
    intDim = config['intDim']

    if n != 0:
        digit(
            digit = n,
            x = topLeft_x+col*intDim+18,
            y = topLeft_y-row*intDim-intDim+12, 
            style = 'normal',
            myPen = myPen
        )



def print_sudoku(sudoku):
    '''
        This function prints the whole sudoku.
    '''

    myPen = initialize_turtle()
    drawGrid(myPen)
    print_digits(sudoku, myPen)