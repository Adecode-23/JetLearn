from random import randint

def Grid():
    Megalist=[]
    for i in range(5):
        s=[]
        for j in range(5):
            s.append("_")
        Megalist.append(s)
    return Megalist

def place_treasure(grid):
    treasure_row = randint(0, 4)
    treasure_col = randint(0, 4)
    return treasure_row, treasure_col

def give_hint(treasure_row, treasure_col, row, col):
    if row < treasure_row:
        return "The treasure is below your guess."
    elif row > treasure_row:
        return "The treasure is above your guess."
    elif col < treasure_col:
        return "The treasure is to the right of your guess."
    elif col > treasure_col:
        return "The treasure is to the left of your guess."
    else:
        return (f"Congratulations! You found the treasure in {attempts} attempts!")

grid=Grid()
treasure_row, treasure_col = place_treasure(grid)
print("Welcome to the Treasure Hunt Game!")
attempts=0
while True:
    print("\nCurrent Grid:")
    for row in grid:
        print(" ".join(row))
    
    row = int(input("Enter the row number (0-4): "))
    col = int(input("Enter the column number (0-4): "))
    
    if row not in range(5) or col not in range(5):
        print("Invalid input. Please enter numbers between 0 and 4.")
        continue    
    attempts += 1
    if treasure_row == row and treasure_col == col:
        print(f"Congratulations! You found the treasure in {attempts} attempts!")
        break
    else:
     hint = give_hint(treasure_row, treasure_col, row, col)
     print(hint)
