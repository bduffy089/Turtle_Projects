
# This program creates house
# Britney Duffy 

import turtle

turtle.shape("square")  # optional
turtle.speed(5)  # optional
turtle.pensize(5)

def square(len):
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)
def triangle(len):
    for i in range(3):
        turtle.forward(len)
        turtle.left(120)

def rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
def house(len):
    square(size)
    triangle(size)

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

# house one
turtle.color("maroon1")
house(100)
back(150)
# house two
turtle.color("aqua")
house(120)


turtle.Screen().exitonclick()
