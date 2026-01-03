from art import LOGO
import random

print(LOGO)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

difficultyLevel = 10 if difficulty == "easy" else 5

numberOptions = [i for i in range(1, 100 + 1)]

numberPicked = random.choice(numberOptions)

guess = 0

while difficultyLevel > 0 and guess != numberPicked:
    print(f"You have {difficultyLevel} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    if guess != numberPicked:
        if guess > numberPicked:
            print("Number to high")
        else:
            print("Number to low")

        difficultyLevel -= 1

        if difficultyLevel > 0:
            print(f"Guess again.")

if guess == numberPicked:
    print(f"You got it! The answer was {numberPicked}")
else:
    print(f"Number was {numberPicked}")
