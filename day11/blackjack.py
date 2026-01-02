from art import logo
import random

print(logo)

play = "y"


def getCard() -> int:
    """
    Returns a card value between 1 and 11
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)


def calculateScore(cards) -> int:
    """
    Returns the score given a back of card values

    :param cards: Pack of cards
    :return: returns the total score
    :rtype: int
    """
    total = 0
    for card in cards:
        total += card

    return total


def printScorePlayer(cards, total):
    print(f"Player cards are: {cards}. Current score {total}")


while play == "y":

    playerCards = []
    computerCards = []

    for i in range(0, 2):
        playerCards.append(getCard())
        computerCards.append(getCard())

    totalScore = 0
    totalScore = calculateScore(playerCards)
    printScorePlayer(playerCards, totalScore)
    print(f"Computers first card is {computerCards[0]}")

    if totalScore < 21:

        newCard = input("Do you want an additional card? y or n ")

        while newCard == "y":
            playerCards.append(getCard())
            totalScore = calculateScore(playerCards)
            if totalScore > 21 and 11 in playerCards:
                newCards = []
                for card in playerCards:
                    if card == 11:
                        newCards.append(1)
                    else:
                        newCards.append(card)
                playerCards = newCards
                totalScore = calculateScore(playerCards)
            printScorePlayer(playerCards, totalScore)

            if totalScore < 21:
                newCard = input("Do you want an additional card? y or n ")
            elif totalScore == 21:
                newCard = "n"
            else:
                newCard = "n"

    if totalScore > 21:
        print("Bust")
    else:
        computerScore = calculateScore(computerCards)
        while computerScore <= 18:
            computerCards.append(getCard())
            computerScore = calculateScore(computerCards)
            if computerScore > 21 and 11 in computerCards:
                newCards = []
                for card in computerCards:
                    if card == 11:
                        newCards.append(1)
                    else:
                        newCards.append(card)
                computerCards = newCards
                computerScore = calculateScore(computerCards)

        print(f"Computer final cards are: {computerCards} with score {computerScore}")

        if computerScore > 21:
            print("You Win!")
        elif computerScore == totalScore:
            print("Draw")
        elif computerScore < totalScore:
            print("You Win!")
        else:
            print("You Loose!")

    play = input("Do you want to play a game of BlackJack? y or n ")
