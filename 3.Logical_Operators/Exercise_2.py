# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = weight / (height * height)
bmi = round(bmi)

text = ""

if bmi <= 18.5:
    text = "are underweight"
elif bmi <= 25:
    text = "have a normal weight"
elif bmi <= 30:
    text = "are slightly overweight"
elif bmi <= 35:
    text = "are obese"
else:
    text = "are clinically obese"

print(f"Your BMI is {bmi}, you {text}.")
