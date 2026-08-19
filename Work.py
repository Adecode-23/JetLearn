import turtle,time
from random import randint
from random import choice
pen=turtle.Turtle()
bg=turtle.Screen()
bg.bgcolor("black")

def draw_star(size, color):
    pen.color(color)
    pen.begin_fill()
    for i in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()

move_distance = randint(200, 400)
size=randint(50, 300)


chacolor=["red", "blue", "green", "yellow", "purple", "orange"]

start_time = time.time()

for i in range(5):
    draw_star(size, choice(chacolor))
    pen.penup()
    pen.right(move_distance)
    pen.forward(move_distance)
    pen.pendown()

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

