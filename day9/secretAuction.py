import os
from art import logo

print(f"{logo}\n\n")

moreBidders = "yes"

bidders = {}

while moreBidders == "yes":
    bidder = input("What is the bidders name? ").lower()
    bid = float(input("What is their bid? R"))

    bidders[bidder] = bid

    moreBidders = input("Are there more bidders? yes or no ").lower()

    os.system("cls")

highestbid = None

for k, v in bidders.items():
    if highestbid == None:
        highestbid = k
    elif bidders[highestbid] < v:
        highestbid = k

print(f"The highest bid was by {highestbid} for value of R{bidders[highestbid]}!")
