MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

def change_calculator(order):
    print("Please insert coins.")
    quarters = float(input("How many quarters? : "))
    dimes = float(input("How many dimes? : "))
    nickles = float(input("How many nickles? : "))
    pennies = float(input("How many pennies? : "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    change = round(total - MENU[order]["cost"], 2)
    if MENU[order]["cost"] > total:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${change} in change.")
        print(f"Here is your {order} ☕️. Enjoy!")
        return MENU[order]["cost"]

def out_of(order):
    for item in resources:
        if MENU[order]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return True
    return False

machine_off = False
money = 0

while not machine_off:
    order = input("What would you like? (espresso/latte/cappuccino) : ")
    if order == "off":
        machine_off = True
    elif order == "report":
        print(f"Water : {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffee : {resources['coffee']}")
        print(f"Money : {money}")
    else:
        if not out_of(order):
            for item in resources:
                resources[item] -= MENU[order]["ingredients"][item]
            money += change_calculator(order)
        
