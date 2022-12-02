from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_off = False

while not machine_off:
    options = menu.get_items()
    user_input = input(f'What would you like ({options}): ')
    if user_input == 'off':
        machine_off = True
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        cost = drink.cost
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(cost)
            coffee_maker.make_coffee(drink)