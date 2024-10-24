from os import system

bid_dictionary = {}

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bid_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Main program
print("Welcome to the secret auction program")
continue_bidding = True
choice = "yes"
while choice == 'yes':
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    choice = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    bid_dictionary[name] = price

    system("cls")
    if choice == "no":
        continue_bidding = False
        find_highest_bidder(bid_dictionary)
