from data import MENU, resources

def check_money():
    return



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
        elif choice == 'espresso':
            
        
coffee_machine()