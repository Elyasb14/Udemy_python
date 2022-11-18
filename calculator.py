import math


# calculating functions

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# dictionary for operations
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
    }

# main calculator function
def calculator():
    continue_calculating = True
    # input first number
    n1 = float(input('Enter your first number: '))
    # main while loop
    while continue_calculating:
        # input second number 
        n2 = float(input('Enter your second number: '))\
        # choose operation
        operation_symbol = input('Enter the operation youd like to use: +, -, *, /, **, %: ')
        # check to not divide by 0
        if operation_symbol == '/' and n2 == 0:
            print('Cannot divide by zero')
            n1 = float(input('Input your first number: '))
            continue
        operation = operations[operation_symbol]
        answer = operation(n1, n2)
        print(answer)
        # ask user if they want to continue
        user_continue = input("Do you want to do more? Or clear and start over? ").lower()
        if user_continue == 'yes':
            n1 = answer
        elif user_continue == 'over':
            # recursion
            calculator()
        else:
            print('Goodbye')
            continue_calculating = False

# call the main function
calculator()
