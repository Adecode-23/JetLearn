

def Grid():
    Megalist=[]
    for i in range(5):
        s=[]
        for j in range(5):
            s.append("_")
        Megalist.append(s)
    return Megalist



grid=Grid()
print("Welcome to the Treasure Hunt Game!")
attempts=0
while True:
    print("Current Grid:")
    for row in grid:
        print(" ".join(row))
    
    row = int(input("Enter the row number (0-4): "))
    col = int(input("Enter the column number (0-4): "))
    
    #if row not in 