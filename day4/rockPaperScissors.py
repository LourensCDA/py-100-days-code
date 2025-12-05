import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

gameScope = [rock, paper, scissors]

userInput = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n")
)

if userInput <= len(gameScope) - 1:
    print(gameScope[userInput])
else:
    print("Invalid Selection")
    exit()

computerChoice = random.randint(0, len(gameScope) - 1)

print(f"Computer choice: \n {gameScope[computerChoice]}")


if userInput == computerChoice:
    print("It is a draw")
elif (
    (userInput == 0 and computerChoice == 2)
    or (userInput == 1 and computerChoice == 0)
    or (userInput == 2 and computerChoice == 1)
):
    print("You win!")
else:
    print("You loose")
