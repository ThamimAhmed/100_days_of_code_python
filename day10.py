# Calculator
from os import system
def addition(num1,num2):
    result = num1 + num2
    return result

def subtraction(num1,num2):
    result = num1 - num2
    return result

def multiplication(num1,num2):
    result = num1 * num2
    return result

def division(num1,num2):
    result = num1 / num2
    return result

operations = {
    "+" : addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    }

def calculator():
    should_accumulate = True
    num1 = float(input("Enter your first number: "))

    while should_accumulate:

        num2 = float(input("Enter your second number: "))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        answer = operations[operation_symbol](num1,num2)
        print(f" {num1} {operation_symbol} {num2} = {answer} ")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to stop: ").lower()
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            system("cls")
            calculator()

calculator()