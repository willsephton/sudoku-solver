
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
