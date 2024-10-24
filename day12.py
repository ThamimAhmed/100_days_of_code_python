import random
from os import system
# easy is 10 guesses
# hard is 5 guesses
# Random number
randomNum = random.randint(1,100)

# Compare user guess with random number
def compare(turns) -> None:
    system("cls")
    for x in range(turns):
        print(f"You have {turns} attempts remaining to guess the number. ")
        guess = int(input("Make a guess: "))
        if guess == randomNum:
            print(f"You got it. The answer was {randomNum}")
            break
        elif guess < randomNum:
            print("Too low")
            print("Guess again")
            turns -= 1
        elif guess > randomNum:
            print("Too high")
            print("Guess again")
            turns -= 1

# Setting difficulty
def setDiff() -> int:
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff == "easy":
        return 15
    elif diff == "hard":
        return 10
    else:
        print("Enter a valid input. ")
        return 0

# Main Code    
print("Welcomme to the numbers guessing game!")
print("I'm thinking of a number between 1 and 100.")
print(randomNum)
turns = 0
while turns == 0:
    turns = setDiff()
compare(turns)