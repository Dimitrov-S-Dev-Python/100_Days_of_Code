# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

pays_the_bill = random.choice(names)
print(f"{pays_the_bill} is going to buy the meal today!")
