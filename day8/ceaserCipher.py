import string
from art import logo

alphabet = list(string.ascii_lowercase)


def encrypt(word: str, shift: int):
    encryptedWord = ""
    for w in word:
        if w.lower() in alphabet:
            currentIndex = alphabet.index(w.lower())
            newIndex = currentIndex + shift
            newIndex %= len(alphabet)
            encryptedWord += alphabet[newIndex]
        else:
            encryptedWord += w

    return encryptedWord


def decrypt(encryptedWord: str, shift: int):
    decryptedWord = ""
    for w in encryptedWord:
        if w.lower() in alphabet:
            currentIndex = alphabet.index(w.lower())
            newIndex = currentIndex - shift
            newIndex %= len(alphabet)
            decryptedWord += alphabet[newIndex]
        else:
            decryptedWord += w

    return decryptedWord


def ceasar(direction: str, word: str, shift: int):
    result = ""
    if direction == "encrypt":
        print(encrypt(word, shift))
    else:
        print(decrypt(word, shift))


print(f"{logo}\n\n")

repeat = "Yes"

while repeat == "Yes":
    getDirection = input("What is the direction? encrypt or decrypt: ")
    getWord = input("What is the word? ")
    getShift = int(input("How much should it shift? "))

    ceasar(getDirection, getWord, getShift)

    repeat = input("Do you want to go again? Yes or No: ")

print("goodbye")
