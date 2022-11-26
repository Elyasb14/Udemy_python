from game_data import data
import random
score = 0
person1 = random.choice(data)
# print(person1)
followers_1 = person1['follower_count']
# print(followers_1)
end_of_game = False

while not end_of_game:
