

import random

health_easy = 10
health_hard = 5

def compare(number, guess, turns):
    if guess > number:
        print('Too high.')
        return turns -1
    elif guess < number:
        print('Too low.')
        return turns -1
    else:
        print(f'You win! the answer was {number}')

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return health_easy
    else:
        return health_hard

def game():
    number = random.randint(1, 100)
    print(f"Pssst, the correct answer is {number}") 

    turns = set_difficulty()
    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")

        #Let the user guess a number.
        guess = int(input("Make a guess: "))

        #Track the number of turns and reduce by 1 if they get it wrong.
        turns = compare(number, guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")
            
game()
