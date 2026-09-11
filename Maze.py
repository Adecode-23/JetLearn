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
                tile.speed(1000)
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
player.speed(0)
player.goto(-226,226)

def check_valid(x,y):
   for tile in tiles:
      if tile.xcor()==x and tile.ycor()==y:
        return False
   return True



def go_up():
    new_x=player.xcor()
    new_y=player.ycor()+24
    if check_valid(new_x,new_y):
        player.goto(new_x,new_y)    

def go_down():
    new_x=player.xcor()
    new_y=player.ycor()-24
    if check_valid(new_x,new_y):
        player.goto(new_x,new_y)        

def go_left():
    new_x=player.xcor()-24
    new_y=player.ycor()
    if check_valid(new_x,new_y):
        player.goto(new_x,new_y)

def go_right():
    new_x=player.xcor()+24
    new_y=player.ycor()
    if check_valid(new_x,new_y):
        player.goto(new_x,new_y)

sc.listen()

sc.onkey(go_up,"w")
sc.onkey(go_down,"s")
sc.onkey(go_left,"a")
sc.onkey(go_right,"d")
sc.onkey(go_right,"D")  




















turtle.mainloop()

