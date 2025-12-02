print(
    '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______lef
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************\n'''
)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = input(
    "You're at a t-juntion, which direction do you want to go?\n\tType 'left' or 'right'\n"
).lower()

if direction == "right":
    print("GAME OVER! You fall in a hole.")
    exit()

swim_or_wait = input(
    "You come to a lake. There is an island in the middle of the lake.\n"
    "\tType 'swim' to swim across or 'wait' to wait for a boat.\n"
).lower()

if swim_or_wait != "wait":
    print("GAME OVER! You get attacked by an angry trout.")
    exit()

door_color = input(
    "You arrive at the island unharmed. There is a house with 3 doors.\n"
    "\tOne red, one yellow and one blue. Which color do you choose?\n"
).lower()

if door_color == "red":
    print("GAME OVER! You are burned by fire.")
    exit()
elif door_color == "blue":
    print("GAME OVER! You are eaten by beasts.")
    exit()
elif door_color == "yellow":
    print("YOU WIN! You found the treasure!")
else:
    print("GAME OVER! You chose a door that doesn't exist.")
    exit()
