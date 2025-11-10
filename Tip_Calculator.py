# Decription
# A simple program for calculating total amount to split into 5 people with 12% tip.

# Step 1 is to create a variable for storing data (total amount) and initialize it to a value 
bill = 150.00
# Step 2 is to calculate the tip (12%) for the total amount
bill_tip = bill * (12 / 100)
# Step 3 is to calculate the result for the bill with the tip (12%)
bill += bill_tip
# Step 4 is to calculate the bill to split into 5
x = bill / 5
# Step 5 is to print the result to the screen
print(x)