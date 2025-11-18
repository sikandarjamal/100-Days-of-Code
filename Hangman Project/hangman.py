# Description
# Hangman -> It's a guessing game between two players(computer and user in this case)
# The computer will choose a random word and the user will try to guess the word by suggesting letters within limited number of times
# The total lives in this case will be 6 -> the total wrong guesses
# Each time the user guesses wrong, the program will print the hangman stages(total 6) from hangmanart.py
# For more details check https://en.wikipedia.org/wiki/Hangman_(game) or just search for Hangman



import random
from hangmanwords import word_list

# make the computer chose a random word for the user
rm_word = random.choice(word_list)
print(rm_word)

from hangmanart import logo,stages
print(logo)



# prints the hint for the user
user_hint = ''
for letter in rm_word:
    user_hint += '_'
print(f'Word to guess -> {user_hint}')

x = [] # whenever the loop restarts, the display variable holding bits of data is gone. This container is for storing that bits of data

total_lives = 6 # total wrong guesses the user has

game_over = False

while not game_over: # loop -> until the total number of letters in the word are guessed or the user runs out of lives
    print(f'Total lives remaining -> {total_lives}')
    guess = input('Guess a letter -> ') # letter
    display = ''

    if guess in x:
        print(f'You already guessed {guess}. Try again.')

    for letter in rm_word:
        if letter == guess:
            display += letter
            x.append(letter)
        elif letter in x:
            display += letter
        else:
            display += '_'
    print('Word to guess -> ' + display)


    if guess not in rm_word:
        total_lives -= 1
        if total_lives == 0:
            game_over = True
            print(f'The word was {rm_word}. You lose.')


    if '_' not in display:
        game_over = True
        print(f'The word was {display}. You win.')

    print(stages[total_lives])

