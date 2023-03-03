import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_pick = int(input())
comp_pick = random.randint(0, 2)
for_print = [rock, paper, scissors]

print(f"Your pick:\n{for_print[user_pick]}")
print(f"Computer pick:\n{for_print[comp_pick]}")

if user_pick == 0 and comp_pick == 2 or user_pick == 2 and comp_pick == 1:
    print("You won!!!")
elif user_pick == comp_pick:
    print("It is a draw!!!")
else:
    print("You lost!!!")
