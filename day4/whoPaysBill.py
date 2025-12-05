import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

number_of_friends = len(friends)
pickNumber = random.randint(0, number_of_friends - 1)

print(f"{friends[pickNumber]} is going to buy the meal today!")
# choice alternative
print(f"{random.choice(friends)} is going to buy the meal today!")
