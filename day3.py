# day3 project improvements: 
# Improve by making each choice its own function
# This helps make conditional statements easier to check

print('''
      
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')

# Treasure Island function(procedure)
def questionnaire():
    # Choice 1
    choice1 = input("Would you like to go left or right? ")
    choice1 = choice1.lower()

    if choice1 == "right":
        print("Game Over")

    elif choice1 ==  "left":

    # Choice 2
        choice2 = input ("Would you like to swim or wait? ")
        choice2 = choice2.lower()
        if choice2 == "swim":
            print("Game Over")
        elif choice2 == "wait":

    # Choice 3
            choice3 = input("Which door will you pick, Red, Blue or Yellow? ")
            choice3 = choice3.lower()
            if choice3 == "red":
                print("Game Over")
            elif choice3 == "blue":
                print("Game Over")
            elif choice3 == "yellow":
                print("You win")
            
            else:
                ("Enter a valid input \n")
                questionnaire()
        else:
            print("Enter a valid input \n")
            questionnaire()
    else:
        print("Enter a valid choice \n")
        questionnaire()

#Start of Treasure island
print('Welcome to Treasure Island' , end ='\n')
print('Your mission is to find the treasure' , end='\n')
questionnaire()

