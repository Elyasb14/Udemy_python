# import modules
import random

# possible words
word_list = ["aardvark", "baboon", "camel"]

# randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)


# ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = str(input("Input a letter: ")).lower()


# loop thru word to check if guess is in word
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")
    
