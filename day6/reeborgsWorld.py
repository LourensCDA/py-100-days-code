# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# this was quite fun and give problem solving practice


def turnAround():
    turn_left()
    turn_left()


def turnRight():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turnRight()
    move()
    turnRight()
    while front_is_clear():
        move()
    turn_left()


def moveUp():
    turn_left()
    while front_is_clear():
        move()


while not at_goal():
    if wall_on_right():
        moveUp()
    elif front_is_clear():
        move()
    else:
        turnRight()
        move()
#     if wall_in_front():
#        jump()
#    elif front_is_clear():
#        move()
