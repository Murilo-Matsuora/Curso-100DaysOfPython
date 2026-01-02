from idlelib.configdialog import changes

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

def print_report(resources):
    for ingredient in resources:
        if ingredient == "water" or ingredient == "milk":
            print(f"{ingredient.title()}: {resources[ingredient]}ml")
        elif ingredient == "coffee":
            print(f"{ingredient.title()}: {resources[ingredient]}g")
        elif ingredient == "money":
            print(f"{ingredient.title()}: ${resources[ingredient]}")

def check_availability(order, resources):
    ingredients = MENU[order]["ingredients"]

    for resource in resources:
        if resource in ingredients:
            if resources[resource] < ingredients[resource]:
                print(f"There's not enough {resource}!")
                return False
    print(f"There is enough resources.")
    return True

def check_payment(order):
    print(f"The {order} costs ${MENU[order]["cost"]}.")
    coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0,
    }
    for coin in coins:
        coins[coin] = int(input(f"How many {coin} will you expend?: "))

    total = coins["quarters"] * 0.25 + coins["dimes"] * 0.1 + coins["nickles"] * 0.05 + coins["pennies"] * 0.01

    change = total - MENU[order]["cost"]
    if change >= 0:
        print("You got it!")
        if change != 0:
            print(f"Your change is ${round(change, 2)}")
        return MENU[order]["cost"]
    else:
        print(f"Not enough money, sorry! 😢")
        return -1

def update_resources(order, resources):
    ingredients = MENU[order]["ingredients"]

    for resource in resources:
        if resource in ingredients:
            resources[resource] -= ingredients[resource]
            print(f"Removed {ingredients[resource]} of {resource}.")

    resources["money"] += MENU[order]["cost"]
    print(f"Added ${MENU[order]['cost']} to wallet.")

    return resources

def coffee_machine():

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0.00,
    }

    end_session = False

    while not end_session:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "off":
            end_session = True
        elif order == "report":
            print_report(resources)
        elif order in MENU:
            if not check_availability(order, resources):
                end_session = True
            else:
                cost = check_payment(order)
                if cost == -1:
                    end_session = True
                elif cost >= 0:
                    resources = update_resources(order, resources)
                    print(f"Enjoy your {order}! 😊")
                else:
                    print("Unexpected result when checking payment. Exiting...")
                    end_session = True



        else:
            print("Not a valid input.")
            end_session = True


coffee_machine()
