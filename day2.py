print("Welcome to the tip calculator! ")
total_bill = float(input("What was the total bill? £"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_split = (total_bill + tip) / people
tip_split = "{:.2f}".format(tip_split)
print(f"Each person should pay: £{tip_split}" )