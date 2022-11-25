
'''
This code has a bug in it. If you choose yes when prompted to go again, 
and then later on the road you choose you don't want to continue, you will keep on going with negative life.

TO DO:
- try and debug
- try and remove break statements
'''

import random

# main game function

def easy():
    health_easy = 10
    number = random.randint(0, 100)
    return number
print(easy())
  

def hard():
    health_hard = 5
