# import modules
import random
from stages import stages, logo
from words import word_list

# start game
print(logo)

# choose word at random from words.py
chosen_word = random.choice(word_list)



# lists for keeping track of progress in game
display = []
health = 6

#For each letter in the chosen_word, add a "_" to 'display'.
for letter in chosen_word:
    display.append('_')

# end of game conditional
end_of_game = False

# prompt the user to guess a letter until there are no more '_' in display and check conditionals
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"you already guessed {guess}")
    # loop thru each index in chosen_word to see if guess is in chosen_word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    # if the guess is not right, decrease health
    if guess not in chosen_word:
        health -= 1
        # if health is 0 end the game
        if health == 0:
            print(f'You lose... the word was {chosen_word}')
            end_of_game = True
    # print the state of the game
    print(f"{' '.join(display)}\n{stages[health]}")
    
    # check if there are any blank spaces in the display; if there are none -> end_of_game = True
    if '_' not in display:
        end_of_game = True
        print('You Win!')       



