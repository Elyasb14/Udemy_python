'''
TO DO:

- If the user guesses right, change personB to personA and generate a new person B

'''

from game_data import data
import random

score = 0
end_of_game = False

def compare(followersA, followersB):
    if followersA > followersB:
        return 'A', personA
    else: 
        return 'B', personB

personA = random.choice(data)
personA_name = personA['name']
followersA = personA['follower_count']

personB = random.choice(data)
personB_name = personB['name']
followersB = personB['follower_count']

while not end_of_game:
    print(f'{personA_name} vs. {personB_name}')
    print(f'person {compare(followersA, followersB)} is the answer.')
    guess = input('Who has more followers, person A or B: ')
    answer = compare(followersA, followersB)
    if guess == answer:
        score += 1
        print(f'Your score is {score}')
        personA = answer
        personB = random.choice(data)
    else:
        print('You were wrong')
        end_of_game = True