def mainMenu():
    runtime = True
    while runtime == True:
        print("\n\n-------Main Menu-------")
        print("1 - Sudoku Solver \n2 - Exit")
        choice = input("Which option would you like to pick: ")
        if choice == "1":
            sudokuSolver()
        elif choice == "2":
            print("Exiting.....")
            runtime = False
            break
        else:
            print("Incorrect option. Please try again.")
 
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
            
def populateGrid(inputGrid):
    print("Please enter \"0\" for empty spaces")
    rows = []
    grid = []
    for y in range(1,10):
        row = rowIfStatement(y) 
        for x in range(1,10):
            number = rowIfStatement(x)

            coloumn = input(f"Please enter the {number} number on the {row} row: ")
            if coloumn == "":
               coloumn = 0
            else:
                coloumn = int(coloumn) 
            rows.append(coloumn)
        grid.append(rows)
        rows = []
    print("\n\nThis is your grid: \n")
    printBoard(grid)
    return grid

def sudokuSolver():
    print("-------Sudoku Solver-------")
    
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
    
    newGrid = populateGrid(inputGrid)
    

def printBoard(inputGrid):
    for i in range(0, 9):
        if i != 0 and i % 3 == 0:
            print("- - - + - - - + - - -")
        for j in range(0, 9):
            if j != 0 and j % 3 == 0:
                print("|", end=" ")
            print(f"{inputGrid[i][j]}", end= " ")
        print()
        
        
        
mainMenu()
