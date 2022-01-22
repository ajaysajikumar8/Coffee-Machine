from data import MENU, resources, profit
from art import logo


def make_coffee(water, milk, coffee, resources):
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee


def calculate_money(quarters, dimes, nickels, pennies):
        user_paid = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
        if user_paid < cost:
            print("Sorry that's not enough money. Money refunded.")
            return 0
        elif user_paid >= cost:
            change = user_paid - cost
            make_coffee(water, milk, coffee, resources)
            print(f"Here is ${change} in change.")
            print("Here is your latte ☕️. Enjoy!")
            return cost


def check_resources(user_input):
    for x in MENU:
        if user_input == x:
            if resources["water"] < MENU[x]["ingredients"]["water"]:
                return "“Sorry there is not enough water."
            elif resources["milk"] < MENU[x]["ingredients"]["milk"]:
                return "“Sorry there is not enough milk."
            elif resources["coffee"] < MENU[x]["ingredients"]["coffee"]:
                return "Sorry there is not enough milk."
            else:
                return 0


machine_running = True
while machine_running:
    print(logo)
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        machine_running = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        resources_check = check_resources(user_choice)
        for x in MENU:
            if user_choice == x:
                water = MENU[x]["ingredients"]["water"]
                milk = MENU[x]["ingredients"]["milk"]
                coffee = MENU[x]["ingredients"]["coffee"]
                cost = MENU[x]["cost"]
                
        if resources_check == 0:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            money = calculate_money(quarters, dimes, nickels, pennies)
            profit += money
        else:
            print(resources_check)
