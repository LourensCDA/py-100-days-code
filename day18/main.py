from turtle import Turtle, Screen, colormode
import random

timmy_the_turtle = Turtle()
colormode(255)

screen = Screen()


# colors_names = ["red", "green", "blue", "cyan", "magenta", "yellow", "black"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


def drawShape(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy_the_turtle.left(angle)
        timmy_the_turtle.forward(100)
    timmy_the_turtle.color(random.choice(random_color()))


def randomWalk(direction):

    timmy_the_turtle.right(direction)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.color(random_color())


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
# timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

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


# for i in range(3, 11):
#     drawShape(i)
numberRange = [i for i in range(10, 40)]

# direction = [0, 90, 180, 270]
# for _ in range(random.choice(numberRange)):
#     randomWalk(random.choice(direction))

i = random.choice(numberRange)
for _ in range(int(360 / i)):
    timmy_the_turtle.circle(50)
    timmy_the_turtle.color(random_color())
    currentHeading = timmy_the_turtle.heading()
    timmy_the_turtle.setheading(currentHeading + int(360 / i))

screen.exitonclick()
