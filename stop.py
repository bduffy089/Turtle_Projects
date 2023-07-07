# Stop Signs Turtles
# by Britney Duffy

import turtle

turtle.shape("square")  # optional
turtle.speed(10)  # optional
turtle.pensize(5)

def forward(len):
    turtle.penup()
    turtle.forward(len)
    turtle.pendown()
def rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
def octagon(len):
    for i in range(8):
        turtle.forward(len)
        turtle.left(45)

def stop(size):
    octagon(size)
    forward(3/8 * size)
    rectangle(1/5 * size, 2 * size)

# draw stop 1
turtle.color("MediumPurple1")
stop(80)
#move pen
forward(170)
#draw stop 2
turtle.color("IndianRed1")
stop(60)

turtle.Screen().exitonclick()