# compare follower counts
"""
1. Get the start value to compare
2. Get the compare value
3. Get response
4. If wrong, game ends show score
5. If correct increment score, remove start value from options and move compare value to start value
"""
import random
from art import logo, vs
from data import data

# get index of options
availableOptions = [i for i in range(0, len(data))]

# pick first start value
startValue = random.choice(availableOptions)

# set score to 0
score = 0

print(logo)

while startValue:
    # remove option
    availableOptions.pop(startValue)

    # get compare value
    compareValue = random.choice(availableOptions)

    print(
        f"Compare A: {data[startValue]["name"]}, a {data[startValue]["description"]}, from {data[startValue]["country"]}"
    )
    print(vs)
    print(
        f"To B: {data[compareValue]["name"]}, a {data[compareValue]["description"]}, from {data[compareValue]["country"]}"
    )

    correctAnswer = (
        "a"
        if data[startValue]["follower_count"] > data[compareValue]["follower_count"]
        else "b"
    )

    numberOfFollowers = input("Who has the highest amount of followers? A or B ")

    if numberOfFollowers.lower() == correctAnswer:
        score += 1
        if correctAnswer == "a":
            print(f"You are correct, {data[startValue]["name"]} has more followers")
        else:
            print(f"You are correct, {data[compareValue]["name"]} has more followers")
        startValue = compareValue
    else:
        if correctAnswer == "a":
            print(
                f"You are wrong, {data[startValue]["name"]} has more followers. Your score is: {score}"
            )
        else:
            print(
                f"You are wrong, {data[compareValue]["name"]} has more followers. Your score is: {score}"
            )
        startValue = None
