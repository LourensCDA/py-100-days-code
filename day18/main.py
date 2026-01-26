from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

screen = Screen()

colors_names = ["red", "green", "blue", "cyan", "magenta", "yellow", "black", "white"]


def drawShape(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy_the_turtle.left(angle)
        timmy_the_turtle.forward(100)
    timmy_the_turtle.color(random.choice(colors_names))


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

# draw a square
# for _ in range(4):
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)

# draw dashed line
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()


for i in range(3, 11):
    drawShape(i)


screen.exitonclick()
