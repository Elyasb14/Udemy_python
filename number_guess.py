
'''
This code has a bug in it. If you choose yes when prompted to go again, 
and then later on the road you choose you don't want to continue, you will keep on going with negative life.

TO DO:
- try and debug
- try and remove break statements
'''

import random

# main game function

def game():
    easy_or_hard = input('Would you like to do easy or hard: ')
    def easy():
        # local easy() variables
        random_integer = random.randint(0, 100)
        health_easy = 10
        end_of_game = False
        # main while loop
        while not end_of_game:
            # checking if health is 0 to either end game or try another number
            if health_easy < 1:
                print(f'the answer was {random_integer}')
                go_again = input('would you like to go again: ')
                if go_again == 'yes':
                    game()
                elif go_again == 'no':
                    break
            # user guess
            user_input = int(input('Submit a guess between 1 and 100: '))
            # comparing guess to random integer
            if user_input > random_integer:
                print('Your guess is too high')
                health_easy -= 1
                print(f' you have {health_easy} more guesses left')
            elif user_input < random_integer:
                print('Your guess is too low')
                health_easy -= 1
                print(f'you have {health_easy} more guesses left')
            else:
                print('You guesed right!')
                # check and see if user wants to go again
                go_again = input('would you like to go again: ')
                if go_again == 'yes':
                    game()
                elif go_again == 'no':   
                    break

    def hard():
        # local hard() variables
        random_integer = random.randint(0, 100)
        health_hard = 5
        end_of_game = False
        # main while loop
        while not end_of_game:
            # check to see if user has zero health and check if user wants to quit or try another number
            if health_hard < 1:
                print(f'the answer was {random_integer}')
                go_again = input('would you like to go again: ')
                if go_again == 'yes':
                    game()
                elif go_again == 'no':
                    break
            # user guess
            user_input = int(input('Submit a guess between 1 and 100: '))
            # comparing guess to random_integer
            if user_input > random_integer:
                print('Your guess is too high')
                health_hard -= 1
                print(f'you have {health_hard} more guesses left')
            elif user_input < random_integer:
                print('Your guess is too low')
                health_hard -= 1
                print(f'you have {health_hard} more guesses left')
            else:
                print('You guesed right!')
                # ask if user wants to go again
                go_again = input('would you like to go again: ')
                if go_again == 'yes':
                    game()
                elif go_again == 'no':
                    break
    if easy_or_hard == 'easy':
        easy()
    elif easy_or_hard == 'hard':
        hard()

game()