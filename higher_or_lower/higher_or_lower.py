from game_data import data
import random

score = 0
end_of_game = False

def compare(followersA, followersB):
    if followersA > followersB:
        return 'A'
    else: 
        return 'B'
    

while not end_of_game:
    personA = random.choice(data)
    personA_name = personA['name']
    followersA = personA['follower_count']
    personB = random.choice(data)
    personB_name = personB['name']
    followersB = personB['follower_count']
    print(f'{personA_name} vs. {personB_name}')
    print(f'person {compare(followersA, followersB)} is the answer.')
    guess = input('Who has more followers, person A or B: ')
    answer = compare(followersA, followersB)
    if guess == answer:
        score += 1
        print(f'Your score is {score}')
    else:
        print('You were wrong')
        end_of_game = True