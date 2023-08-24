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

#Write your code below this line 👇

options=["rock","paper","scissor"]
user_choice=input(f"Enter Your choice from rock paper scissor!\nRock{rock}Paper{paper}Scissor{scissors}")
computer_choice=random.choice(options)
if user_choice==computer_choice:
    print(f"{user_choice,computer_choice} its a draw!")
elif user_choice=="rock" and computer_choice=="scissor" or user_choice=="scissor" and computer_choice=="paper" or \
        user_choice=="paper" and computer_choice=="rock":
    print(f"{user_choice,computer_choice} You Won!!")
else:
    print(f"{user_choice, computer_choice} You lost!")