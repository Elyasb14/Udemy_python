

from game_data import data
import random

def get_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}."

def compare(followersA, followersB, guess):
    if followersA > followersB:
        return guess == 'a'
    else:
        return guess == 'b'
    
def game():
    score = 0
    end_of_game = False
    accountA = get_account()
    accountB = get_account()
    while not end_of_game:
        accountA = accountB
        accountB = get_account()
        while accountA == accountB:
            accountB = get_account()
        print(f"Compare A: {format_data(accountA)}.")
        print('vs')
        print(f"Against B: {format_data(accountB)}.")
        guess = input('Input who you think has more followers: ').lower()
        followersA = accountA['follower_count']
        followersB = accountB['follower_count']
        is_correct = compare(followersA, followersB, guess)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            end_of_game = True
            print('you lose...')
                
game()
                
            