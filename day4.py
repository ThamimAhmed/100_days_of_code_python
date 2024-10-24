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

print("Welcome to the Rock-Paper-Scissors game. ")

sign = [rock, paper, scissors]

try:
    user_choice = int(input("Choose: 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print("Your Choice:")
    print(sign[user_choice] , end="\n")

    computer_choice = random.randint(0,2)
    print("The Computer's Choice:")
    print(sign[computer_choice] , end="\n")


    if user_choice < 0 or user_choice > 2:
        print("You didn't type a valid option so you lose")
    else:
        if (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0) or (user_choice > computer_choice):
            print("You Win")
        elif user_choice < computer_choice:
            print("You Lose")
        elif user_choice == computer_choice:
            print("Draw")
        else:
            print("Something went wrong")
except ValueError as ve:
    print("Make sure you enter a NUMBER.")