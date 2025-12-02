height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Write your code here.
# Calculate the bmi using weight and height.
bmi = float(weight) / (float(height) ** 2)
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")
