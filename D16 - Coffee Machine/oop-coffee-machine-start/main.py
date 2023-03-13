from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_m = MoneyMachine()
machine = CoffeeMaker()
options = Menu()
a = True

while a:
    prompt = input(f"What would you like? {options.get_items()}: ")
    if prompt.lower() == "report":
        machine.report()
        money_m.report()
    elif prompt.lower() == "off":
        a = False
    else:
        choice = options.find_drink(prompt)
        if choice is None:
            a = True
        elif machine.is_resource_sufficient(choice) and money_m.make_payment(choice.cost):
            machine.make_coffee(choice)
