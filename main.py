
# Sudoku Solver Program with AI Backtracing Algorithm - Will Sephton

def mainMenu():
    runtime = True 
    while runtime == True: # Starts the while loop for validation on the menu
        print("\n\n-------Main Menu-------")
        print("1 - Sudoku Solver \n2 - Exit")
        choice = input("Which option would you like to pick: ")
        if choice == "1":
            sudokuSolver() # Runs the solver
        elif choice == "2":
            print("Exiting.....")
            runtime = False
            break
        else:
            print("Incorrect option. Please try again.")
 
# If statement for converting loop numbers into English terms  
 
def rowIfStatement(number):
    if number == 1:
        number = "first"
    elif number == 2:
        number = "second"
    elif number == 3:
        number = "third"
    elif number == 4:
        number = "fourth"
    elif number == 5:
        number = "fifth"
    elif number == 6:
        number = "sixth"
    elif number == 7:
        number = "seventh"
    elif number == 8:
        number = "eigth"
    elif number == 9:
        number = "ninth"
    else:
        number = "error"   
    return number         
            
# The function for allowing the user to enter their grid            

def populateGrid(inputGrid):
    #This is how we will figure out the empty squares
    print("Please enter \"0\" for empty spaces")
    
    # Declaring the Lists
    rows = []
    grid = []
    
    # For loop to go through each row of nine, nine times.   
    for y in range(1,10):
        row = rowIfStatement(y) # Gets the English term for what row the program is on
        for x in range(1,10):
            number = rowIfStatement(x) # Gets the English term for what number the program is on

            coloumn = input(f"Please enter the {number} number on the {row} row: ") # Asks the user to input their number
            # If someone does not enter a number it will be counted as 0
            if coloumn == "":
               coloumn = 0
            else:
                coloumn = int(coloumn) # Converts the string input into an integer
            rows.append(coloumn) # Adds that number to the row list
        grid.append(rows) # Adds that row list to a grid array
        rows = [] # Clears the row list for the next row
    print("\n\nThis is your grid: \n") 
    printBoard(grid) # Displays the users inputted grid
    return grid # Returns the grid

# The row, coloumn and square test functions

def rowTest(newGrid,row,currentNumber):
    # For loop going through the numbers 1 to 10 (but not including 10) to check every number on the row
    for x in range(1,10): 
        if currentNumber==newGrid[row][x]: # If the current number (0-9) is already in the row then it can't exist there
            return False # Returning False to show the space can not allow the current number
    return True # Returning True to show the space can allow the current number

def coloumnTest(newGrid,coloumn,currentNumber):
    # For loop going through the numbers 1 to 10 (but not including 10) to check every number on the coloumn
    for x in range(1,10): 
        if currentNumber==newGrid[x][coloumn]: # If the current number (0-9) is already in the column then it can't exist there
            return False # Returning False to show the space can not allow the current number
    return True # Returning True to show the space can allow the current number
    
def sqaureTest(grid,row,coloumn,currentNumber):
    #Finding the center
    row=(row//3)*3+1
    coloumn=(coloumn//3)*3+1
    # Defining the numbers used in the for loops to check every number in the cell
    movingNumbers = [-1,0,1]
    # For loops going through each number in the square 
    for x in movingNumbers:
        for y in movingNumbers:
            if grid[x+row][y+coloumn] == currentNumber: # If the current number (0-9) is already in the box then it can't exist there
                return False # Returning False to show the space can not allow the current number
    return True # Returning True to show the space can allow the current number

# Function to find any 0's on the grid

def findZeros(grid):
    for x in range(1,10): # For loop through all the row
        for y in range(1,10): # For loop for all the numbers in a row
            if grid[x][y]==0: # If the number on the grid is a zero then
                return x,y # Returning "coords" for where the number zero is on the grid
    return 10,10 # If there is no zeros left on the grid then return two tens as they are out of bounds of the grid
    

# Main Sudoku Solver function

def sudokuSolver():
    print("-------Sudoku Solver-------") # Title for the solver
    
    # Test grid
    
    """inputGrid =[
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]"""
    
    newGrid = populateGrid() # Creates the grid through user input 
    
    
# Printing the board

def printBoard(newGrid): # Accepts the newGrid as a parameter
    for i in range(0, 9):
        if i != 0 and i % 3 == 0:
            print("- - - + - - - + - - -")
        for j in range(0, 9):
            if j != 0 and j % 3 == 0:
                print("|", end=" ") # Prints the line and allows for values to be printed on the same line
            print(f"{newGrid[i][j]}", end= " ") # Prints the certain row numbers, current number on the grid
        print()
        
        
        
mainMenu()
