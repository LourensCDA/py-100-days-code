fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(f"{fruit} pie")

student_scores = [180, 124, 165, 173, 189, 182, 246]
totalScore = sum(student_scores)
print(totalScore)
totalScore = 0
for score in student_scores:
    totalScore += score
print(totalScore)


highestNumber = max(student_scores)
print(highestNumber)

highestNumber = 0
for score in student_scores:
    if score > highestNumber:
        highestNumber = score

print(highestNumber)

# range
# between 1 and 10, so 1 to 9
for i in range(1, 10 + 1):
    print(i)
for i in range(1, 10 + 1, 3):
    print(i)

# gauls challenge
totalOf = 0
for i in range(1, 100 + 1):
    totalOf += i
print(totalOf)
