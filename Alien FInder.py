from random import randint
import time

def Grid():
    Megalist=[]
    for i in range(6):
        s=[]
        for j in range(6):
            s.append("👤")
        Megalist.append(s)
    return Megalist

def place_treasure(grid):
    treasure_row = randint(0, 5)
    treasure_col = randint(0, 5)
    return treasure_row, treasure_col

def give_hint(treasure_row, treasure_col, row, col):
    if row < treasure_row:
        return "Anamolie is Down south"
    elif row > treasure_row:
        return "Anamolie is Up north"
    elif col < treasure_col:
        return "Anamolie is to the East"
    elif col > treasure_col:
        return "Anomolie is to the West"
    else:
        return (f"Well done You Have found the anamolie in {attempts} attempts!")

grid=Grid()
treasure_row, treasure_col = place_treasure(grid)
print("Help us find the Anamolie! The grid is 6x6. Enter row and column numbers between 0 and 5 to search for the Anamolie.")
attempts = 0

while attempts < 4:
    # ask for input / check answer here
    attempts += 1

    if attempts == 4:
        print("Too late,The anamolie Has spread to the entire grid! Better luck next time.")
while True:
    print("\nCurrent Grid:")
    for row in grid:
        print(" ".join(row))
    
    row = int(input("Enter the y coordinate (0-5): "))
    col = int(input("Enter the x coordinate (0-5): "))
    
    if row not in range(6) or col not in range(6):
        print("Invalid input. Please enter numbers between 0 and 5.")
        continue    
    attempts += 1
    if treasure_row == row and treasure_col == col:
        print(f"Well done You Have found the anamolie in {attempts} attempts!")
        grid[row][col] = "👽"
        print("\nCurrent Grid:")
        for row in grid:
            print(" ".join(row))
        break
    else:
     grid[row][col] = "🧑" 
     hint = give_hint(treasure_row, treasure_col, row, col)
     print(hint)

time.sleep(10)

