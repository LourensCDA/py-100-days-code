from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

screen = Screen()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

# draw a square
for i in range(1, 5):
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)


screen.exitonclick()
