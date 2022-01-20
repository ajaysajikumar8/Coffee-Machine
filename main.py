
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



money = 0 

#Ask the user input for what they would like to have?
user_choice = input("What would you like? (espresso/latte/cappuccino): ")

#check what the user input was and then further execute
for x in MENU:
    if user_choice == x:
        water = MENU[x]["ingredients"]["water"]
        milk = MENU[x]["ingredients"]["milk"]
        coffee = MENU[x]["ingredients"]["coffee"]
        cost = MENU[x]["cost"]
        print(water, milk, coffee, cost)

def calculate_money(quarters, dimes, nickels, pennies):
    user_paid = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    if user_paid < cost:
        print("Sorry that's not enough money. Money refunded.")
    elif user_paid >= cost:
        change = user_paid - cost
        print(change)
    


#check if there are resources to make what the user wants.

#if there are sufficient resources then ask the user for moeny

#ask the user how they want to pay (for eg: how many quarters, nickels, dimes, pennies etc)
print("Please insert coins.")
quarters = int(input("How many quarters?: "))
dimes = int(input("How many dimes?: "))
nickels = int(input("How many nickels?: "))
pennies = int(input("How many pennies?: "))
calculate_money(quarters, dimes, nickels, pennies)

#calculate the monetary value of the coins inserted. (make a function)

    

#count the money
    #if insufficient balance return the money
    #return the balance

#provide an off switch to turn off the machine

#the amount of resources required to make the coffee should be reduced from the main resources

#after resources are deducted and tell the user that your coffee is made. 