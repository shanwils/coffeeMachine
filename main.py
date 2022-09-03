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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def has_enough(needed_ingredients):
    """Returns true if order can be made, false if not"""
    for item in needed_ingredients:
        if needed_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        return True


def process_money():
    """Returns the total amount of money inserted"""
    print(f"Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transaction_successful(money_inserted, drink_cost):
    """Returns true if enough money is inserted, false if insufficient funds"""
    if money_inserted >= drink_cost:
        change = round(money_inserted - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Insufficient funds added. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True

while is_on:
    choice = input("What would you like? (espresso $1.50/latte $2.50/cappuccino $3.00): ")
    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if has_enough(drink["ingredients"]):
            payment = process_money()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])









