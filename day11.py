#BlackJack
import random
from os import system


# To deal the players and the computers cards
def deal_cards():
    cards = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

        
# To calculate both user and computer score
def calculate_score(cards):
    # Calculate how close to 21
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# To compare both scores to see who wins
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You Lose"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over 21 so You Lose"
    elif c_score > 21:
        return "Opponent went over 21 so You Win"
    elif u_score > c_score:
        return "You Win"
    else: 
        return "You Lose"


# Play game
def play_game():

    is_game_over = False
    user_cards = []
    cpu_cards = []
    user_score = -1
    cpu_score = -1


    for x in range(2):
        user_cards.append(deal_cards())
        cpu_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {cpu_cards[0]}")

        if user_score == 0 or cpu_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_cards())
        cpu_score = calculate_score(cpu_cards)

    system("cls")
    print(f"Your cards: {user_cards}, score: {user_score}")
    print(f"Computer cards: {cpu_cards} score: {cpu_score} ")
    print(compare(user_score,cpu_score))

# Main Code
play_game()
while input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    system("cls")
    play_game()
print("Thank you for playing")