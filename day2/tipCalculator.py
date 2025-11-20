print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? R"))
tip = float(input("How much tip would you like to give? 10, 12, 15? ")) / 100
people = int(input("How many people to split the bill? "))

bill *= 1 + tip

print(f"Each person should pay: R{round(bill/people,2)}")
