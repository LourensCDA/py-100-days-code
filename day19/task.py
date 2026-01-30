from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def moveForwards():
    tim.forward(10)


screen.listen()

screen.onkey(key="space", fun=moveForwards)

screen.exitonclick()
