from data import MENU, resources

def espresso():
    return water - 100, coffee - 50

def latte():
    return water - 100, coffee - 50, milk - 50

def cappuccino():
    return water - 100, coffee - 50, milk -100

def input_money():
    pass

def coffee_machine():
    machine_off = False
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = 0
    while not machine_off:
        choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if choice == 'off':
            return
        elif choice == 'report':
            print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}')

coffee_machine()