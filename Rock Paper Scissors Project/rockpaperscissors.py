import random
import art

# Description
# A simple program for practicing lists
# Help a fellow programmar by sharing your ideas, please don't hesitate to do so

chose = ['rock', 'paper', 'scissors'] # user can chose only one item from the list
itemX = input('Enter rock, paper or scissors -> ').lower() # user itemX from the list
itemX_Index = chose.index(itemX) # itemX index from the list
print(art.logos[itemX_Index])
itemY = random.choice(chose) # computer itemY from the list
itemY_Index = chose.index(itemY) # itemX index from the list
print(f'Computer chosed -> {art.logos[itemY_Index]}')

# conditions
if itemX_Index == itemY_Index:
    print('draw')
elif itemX_Index < 2 and itemY_Index > 1:
    if itemX_Index == 0:
        print('You win.')
    else:
        print('Computer win.')
elif itemX_Index > 1 and itemY_Index < 2:
    if itemY_Index == 0:
        print('Computer win.')
    else:
        print('You win.')
elif itemX_Index < 2 and itemY_Index < 2:
    if itemX_Index == 0 and itemY_Index == 1:
        print('Computer win.')
    else:
        print('You win.')
print('Game over.')