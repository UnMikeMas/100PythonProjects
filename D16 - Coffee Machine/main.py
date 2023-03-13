import Menu
money = 0


def user_choice():
    going=True
    while going:
        choice = input("What would you like? (espresso/cappuccino/latte): ")
        if choice == "espresso" or choice == "cappuccino" or choice == "latte" or choice == "report" or choice == "off":
            return choice
        else:
            print("We don't have that, select again:/")


def availability_function(w, m, c):
    if Menu.resources['water'] < w:
        return "water"
    elif Menu.resources['milk'] < m:
        return "milk"
    elif Menu.resources['coffee'] < c:
        return "coffee"
    else:
        return 0


def start(money):
    choice = user_choice()
    if choice == "off":
        return print("GoodBye!")
    elif choice == "report":
        print(f"Water: {Menu.resources['water']}\nMilk: {Menu.resources['milk']}\nCoffee: {Menu.resources['coffee']}\nMoney: {money}")
        start(money)
    else:
        water_needed = Menu.MENU[choice]['ingredients']['water']
        milk_needed = Menu.MENU[choice]['ingredients']['milk']
        coffee_needed = Menu.MENU[choice]['ingredients']['coffee']
        availability = availability_function(water_needed, milk_needed, coffee_needed)
        if availability != 0:
            print(f"Sorry there is not enough {availability}")
            start(money)
        print("Please Insert Coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels: "))
        pennies = int(input("How many pennies?: "))
        total_money = round(quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01,2)
        if total_money >= Menu.MENU[choice]['cost']:
            change = total_money - Menu.MENU[choice]['cost']
            print(f"You inserted ${total_money}, the price is ${Menu.MENU[choice]['cost']}, your change is ${change}")
            print(f"Enjoy your {choice}")
            money += Menu.MENU[choice]['cost']
            Menu.resources['water'] -= Menu.MENU[choice]['ingredients']['water']
            Menu.resources['milk'] -= Menu.MENU[choice]['ingredients']['milk']
            Menu.resources['coffee'] -= Menu.MENU[choice]['ingredients']['coffee']
            start(money)
        else:
            print("Sorry that's not enough money. Money refund")
            total_money = 0


start(money)
