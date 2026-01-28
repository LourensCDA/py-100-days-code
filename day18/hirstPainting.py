import colorgram
from pathlib import Path

current_working_directory = Path().resolve() / "day18" / "image.jpg"

colorDict = []

colors = colorgram.extract(current_working_directory, 20)
for color in colors:
    colorDict.append((color.rgb.r, color.rgb.g, color.rgb.b))

# print(colorDict)
from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
colormode(255)

screen = Screen()


# colors_names = ["red", "green", "blue", "cyan", "magenta", "yellow", "black"]
def random_color():
    return random.choice(colorDict)


def restart_position():
    turtle.penup()
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    for _ in range(10):
        turtle.forward(30)
    turtle.setheading(0)
    turtle.pendown()


turtle.penup()
turtle.setheading(225)
turtle.forward(255)
turtle.setheading(0)
turtle.pendown()


for _ in range(10):
    for _ in range(10):
        turtle.penup()
        turtle.dot(20, random_color())
        turtle.forward(30)

    restart_position()


screen.exitonclick()
