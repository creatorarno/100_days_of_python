# Welcome Message
print("Welcome to the Tip Calculator.")

# Ask for the amount needed to pay
total_bill = float(input("What's the total bill: "))

# Ask for how much tip to give
tip = float(input("How much tip would you like to give? 10, 12, 15?: "))

# People to split with
split = int(input("How many people to split with?: "))

# how much you got to pay
print( (total_bill + tip) / split)