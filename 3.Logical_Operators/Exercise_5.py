# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


def get_love(name1, name2):
    num1 = 0
    num2 = 0
    for char in name1.lower():
        for char2 in "true":
            if char == char2:
                num1 += 1

    for char in name2.lower():
        for char2 in "true":
            if char == char2:
                num1 += 1

    for char in name1.lower():
        for char2 in "love":
            if char == char2:
                num2 += 1
    for char in name2.lower():
        for char2 in "love":
            if char == char2:
                num2 += 1

    name_score = str(num1) + str(num2)
    name_score = int(name_score)
    return name_score


score = get_love(name1, name2)

if 10 > score > 90:
    print(f"You score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are all right together.")
else:
    print(f"Your score is {score}.")
