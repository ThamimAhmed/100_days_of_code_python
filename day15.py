# Coffee Machine Program
power = True
resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}
profit = 0
quarters = 0.25
dimes = 0.10
nickles = 0.05 
pennies = 0.01

# Name of coffee: price($), water(ml), coffee(g), milk(ml)
coffee = {
        "espresso": {
            "ingredients" : {
                "water" : 50,
                "coffee" : 18,
                "milk" : 0},
            "price" : 1.50
            },
        "latte": { 
            "ingredients" : {
                "water" : 200,
                "coffee" : 24,
                "milk" : 150},
            "price" : 2.50,
            },
        "cappucino": {
            "ingredients" : {
                "water" : 250,
                "coffee" : 24,
                "milk" : 100},
            "price" : 3.00,
            },
          }

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made and false when ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total calculated from the coins inserted."""
    print("Insert coins. ")
    total = int(input("How many quarters?: "))* 0.25
    total += int(input("How many dimes?: "))* 0.10
    total += int(input("How many nickles?: "))* 0.05
    total += int(input("How many pennies?: "))* 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when te payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. ")


while power == True:
    choice = input("What coffee would you like? 'Espresso', 'latte' or 'cappuccino': ").lower()
    if choice == "off":
        power = False
        quit()
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: ${profit}")
    else:
        drink = coffee[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["price"]):
                make_coffee(choice,drink["ingredients"])