from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


machine_running = True
while machine_running:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ")
    if user_choice == "off":
        machine_running = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if (coffee_maker.is_resource_sufficient(drink)) and  money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)  