print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''') # ASCII Character

# Description
# A simple program for checking the conditions 
# How to program flow 


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Your at a cross road. Where do you want to go?")
left_or_right = input("Type 'left' or 'right'\n")
if left_or_right == "left": # condition one
    print("You've come to a lake. There is an island in the middle of the lack")
    wait_or_swim = input("Type 'wait' to wait for a boat. Type 'swim' to swim\n")
    if wait_or_swim == 'wait': # condition two
        print("You've arrived at the island unharmed. There is a house with three doors.")
        red_or_yellow_or_blue = input("One red, one yellow and one blue. Which color do you chose?\n")
        if red_or_yellow_or_blue == 'yellow': # condition three
            print("You found the treasure! You Win!")
        elif red_or_yellow_or_blue == 'red':
            print("It's a room full of fire. Game over.")
        elif red_or_yellow_or_blue == 'blue':
            print("You enter a room of beasts. Game over")
        else:
            print("Game over.")
    else:
        print("You get attacked by an angry trout. Game over")
else:
    print("You fell into a hole. Game over.")