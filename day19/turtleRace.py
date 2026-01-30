from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


pick = screen.textinput("Make your bet!", "Which turtke will win race? Enter color")
# print(pick)


isRaceOn = True if pick in colors else False

allTurtles = []

yC = -75
for c in colors:
    newT = Turtle("turtle")
    newT.color(c)
    newT.penup()
    newT.goto(x=-225, y=yC)
    yC += 25
    allTurtles.append(newT)

winner = None
while isRaceOn:
    for t in allTurtles:
        randDist = random.randint(0, 10)
        t.forward(randDist)
        if t.xcor() > 250:
            winner = t.color()
            isRaceOn = False

if pick == winner[0]:
    print("You win!")
else:
    print(f"You loose! The {winner[0]} turtle won!")
screen.exitonclick()
