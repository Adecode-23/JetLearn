import turtle

sc=turtle.Screen()
sc.setup(600,600)
sc.bgcolor("skyblue")



maze=["XXXXXXXXXXXXXXXXXXXXX",
      "X XXXXXXXXXXXXXXXXXXX",
      "X XXXXXXXXXXXXXXXXXXX",
      "X XXXXXXXXXXXXXXXXXXX",
      "X XXXXXXXXXXXXXXXXXXX",
      "X XXXXXXXXXXXXXXXXXXX",
      "X XXXXXXXXXXXXXXXXXXX",
      "X XXXXXXXXXXXXXXXXXXX",   
      "X                   X",
      "XXXXXXXXXXXXXXXXXXX X",
      "XXXXXXXXXXXXXXXXXXX X",
      "XXXXXXXXXXXXXXXXXXX X",
      "XXXXXXXXXXXXXXXXXXX X",
      "XXXXXXXXXXXXXXXXXXX X",
      "XXXXXXXXXXXXXXXXXXX X",
      "XXXXXXXXXXXXXXXXXXX X",
      "XXXXXXXXXXXXXXXXXXX X",
      "XXXXXXXXXXXXXXXXXXX X",
      "XXXXXXXXXXXXXXXXXXX X",
      "XXXXXXXXXXXXXXXXXXX X",
      "XXXXXXXXXXXXXXXXXXX X",
      "XXXXXXXXXXXXXXXXXXXFX"]
tiles=[]
food=None
def create_maze():
    global food 
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            character=maze[y][x]
            sc_x=-250+(x*24)
            sc_y=250-(y*24)
            if character=="X":
                tile=turtle.Turtle()
                tile.color("navy")
                tile.shape("square")
                tile.penup()
                tile.speed(0)
                tile.goto(sc_x,sc_y)
                tiles.append(tile)
            elif character=="F":
                food=turtle.Turtle()
                food.color("green")
                food.shape("circle")
                food.penup()
                food.speed(0)
                food.goto(sc_x,sc_y)

create_maze()
player=turtle.Turtle()
player.shape("circle")
player.color("red")
player.penup()
player.speed()
player.goto(-226,226)

def check_valid(x,y):
   for tile in tiles:
      if tile.xcor()==x and tile.ycor==y:
         return False
        return True























turtle.mainloop()

