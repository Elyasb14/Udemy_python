import random
# global health variables
health_easy = 10
health_hard = 5


# function to compere guess and number
def compare(number, guess, turns):
    if guess > number:
        print('Too high.')
        # decrease turns by 1
        return turns - 1
    elif guess < number:
        print('Too low.')
        # decrease turns by 1
        return turns - 1
    else:
        print(f'You win! the answer was {number}')


# function to set difficulty -> returns health_easy or health_hard
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return health_easy
    else:
        return health_hard


# main game function
def game():
    number = random.randint(1, 100)
    # print(f"Pssst, the correct answer is {number}") 
    turns = set_difficulty()
    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = compare(number, guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")
        
game()