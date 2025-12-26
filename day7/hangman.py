import random
from hangmanStages import HANGMANPICS
from hangmanWordlist import word_list


HANGMANPICS.reverse()

# TODO1 - Randomly choose word
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO4 - Placeholder
placeHolder = ""
for i in range(len(chosen_word)):
    placeHolder += "_"

lettersChosen = []


# TODO5 - Update display of placeHolder
def updatePlaceholder(guess, chosen_word, placeHolder):
    temp = [p for p in placeHolder]

    i = 0
    while i < len(chosen_word):
        if chosen_word[i] == guess:
            temp[i] = guess
        i += 1

    returnWord = ""
    for w in temp:
        returnWord += w
    return returnWord


print("Welcome to Hangman Game!")

lives = len(HANGMANPICS) - 1
while "_" in placeHolder:

    print(placeHolder)

    # TODO2 - Ask user to enter letter
    guess = input("Input a letter please: ").lower()

    if guess not in lettersChosen:
        lettersChosen.append(guess)
    else:
        print(f"You've chosen {guess} before!")

    # TODO3 - Check if letter in word or not
    if not guess in chosen_word:
        lives -= 1
        print(f"Wrong! You have {lives} guesses remaining.")

    else:
        placeHolder = updatePlaceholder(guess, chosen_word, placeHolder)

    print(HANGMANPICS[lives])

    if lives == 0:
        print("You lose! The word is " + chosen_word)
        exit()


print("You win! The word is " + chosen_word)
