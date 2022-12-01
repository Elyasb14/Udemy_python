from data import MENU, resources

def request_money(choice):
    if choice == 'espresso':
        cost = MENU['espresso']['cost']
        money_request = float(input(f'input ${cost}: '))
        money = money_request
        return money
    elif choice == 'latte':
        cost = MENU['latte']['cost']
        money_request = float(input(f'input ${cost}: '))
        money = money_request
        return money
    else:
        cost = MENU['cappuccino']['cost']
        money_request = float(input(f'input ${cost}: '))
        money = money_request
        return money

def check_ingredients(choice, water, milk, coffee):
    if MENU['resources']['water'] >  MENU[choice]['ingredients']['water']:
        resources['water'] = resources['water'] - MENU[choice]['ingredients']['water']
        print(resources['water'])
    elif MENU['resources']['milk'] >  MENU[choice]['ingredients']['milk']:
        resources['milk'] = resources['milk'] - MENU[choice]['ingredients']['milk']
        print(resources['milk'])
    elif MENU['resources']['coffee'] >  MENU[choice]['ingredients']['coffee']:
        resources['coffee'] = resources['coffee'] - MENU[choice]['ingredients']['coffee']
        print(resources['coffee'])
check_ingredients('espresso', 'water', "milk", 'coffee')

def coffee_machine():
    machine_off = False
    money = 0
    choice = input('What would you like to drink: ').lower()
    water = MENU[choice]['ingredients']['water']
    milk = MENU[choice]['ingredients']['milk']
    coffee = MENU[choice]['ingredients']['coffee']

    if choice == 'off':
        return
    elif choice == 'status':
        print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}')    
    elif choice == 'espresso':
        money = request_money(choice)
        
        # print(money)
    elif choice == 'latte':
        money = request_money(choice)
        # print(money)
    else: 
        money = request_money(choice)
        # print(money)
    
        
coffee_machine()