from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def moveForwards():
    tim.forward(10)


def moveBackwards():
    tim.backward(10)


def moveLeft():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def moveRight():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    screen.reset()


screen.listen()

screen.onkey(key="w", fun=moveForwards)
screen.onkey(key="s", fun=moveBackwards)
screen.onkey(key="a", fun=moveLeft)
screen.onkey(key="d", fun=moveRight)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
