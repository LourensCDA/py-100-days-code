from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

screen = Screen()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

# draw a square
# for _ in range(4):
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)

# draw dashed line
for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()


screen.exitonclick()
