# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
text = ""
if year % 4 == 0:
    if year % 100 == 0:
        text = "Not Leap"
    elif year % 400 == 0:
        text = "Leap"
    else:
        text = "Leap"
else:
    text = "Not Leap"
print(f"{text} year.")




