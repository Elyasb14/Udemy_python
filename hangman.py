# import modules
import random

# initialize a possible word list
word_list = ["aardvark", "baboon", "camel"]

# choose word at random and print for debugging purposes
chosen_word = random.choice(word_list)
print(chosen_word)


# list for keeping track of progress in game
display = []

#For each letter in the chosen_word, add a "_" to 'display'.
for letter in chosen_word:
    display.append('_')

# end of game conditional
end_of_game = False

# prompt the user to guess a letter until there are no more '_' in display
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # loop thru each index in chosen_word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # check to see if 
        if letter == guess:
            display[position] = guess
    if '_' in display:
        end_of_game = False
    print(display)




