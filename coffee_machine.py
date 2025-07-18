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

initial_amount = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def sufficient_resource(ingredients_needed):
    for item in ingredients_needed:
        if ingredients_needed[item] > initial_amount[item]:
            print(f"Sorry, insufficient {item}.")
            return False
    return True

is_on = True

while is_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {initial_amount['water']}ml")
        print(f"Milk: {initial_amount['milk']}ml")
        print(f"Coffee: {initial_amount['coffee']}ml")
        print(f"Money: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]

        
        if sufficient_resource(drink["ingredients"]):
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))

            total_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

            if total_money >= drink["cost"]:
                change = round(total_money - drink["cost"], 2)
                print(f"Here is ${change} in change.")
                profit += drink["cost"]

                
                for item in drink["ingredients"]:
                    initial_amount[item] -= drink["ingredients"][item]

                print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry, not enough money. Money refunded.")
        
    else:
        print("Invalid option. Please try again")
