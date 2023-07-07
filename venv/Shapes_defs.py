# Basic Shapes
# by Britney Duffy

import turtle

turtle.shape("square")  # optional
turtle.speed(0)  # optional
turtle.pensize(8)

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def triangle(size):
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

def rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def polygon(num, size):
    for i in range(num):
        turtle.forward(size)
        turtle.left(360 / num)

def spiral(len, angle):
    for i in range(len, 5, -5):
        turtle.forward(i)
        turtle.right(angle)

# move functions
def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

# forward helper function
def move(len):
    back(-1 * len)


turtle.Screen().exitonclick()