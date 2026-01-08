from data import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def printReport():
    """
    Prints the current values of resources and money
    """
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}"
    )


def confirmResources(water: int, milk: int, coffee: int) -> str:
    """
    Docstring for confirmResources

    :param option: Description
    :param water: Description
    :type water: int
    :param milk: Description
    :type milk: int
    :param coffee: Description
    :type coffee: int
    :return: Description
    :rtype: string
    """

    if "water" in resources and resources["water"] < water:
        return "water"
    if "milk" in resources and resources["milk"] < milk:
        return "milk"
    if "coffee" in resources and resources["coffee"] < coffee:
        return "coffee"

    return None


def changeResources(water: int, milk: int, coffee: int):
    global resources

    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee


def payment():
    quarters = int(input("Number of quarters: "))
    dimes = int(input("Number of dimes: "))
    nickel = int(input("Number of nickel: "))
    pennies = int(input("Number of pennies: "))

    return quarters * 0.25 + dimes * 0.1 + nickel * 0.05 + pennies * 0.01


machineState = "on"

while machineState == "on":
    machineInput = input(
        "☕ What would you like to drink? espresso/latte/cappuccino "
    ).lower()

    if machineInput == "off":
        machineState = machineInput
        print("Machine is turning off")

    elif machineInput == "report":
        printReport()

    elif machineInput in "espresso/latte/cappuccino":

        itemIngredients = {"water": 0, "milk": 0, "coffee": 0}

        for k, v in MENU[machineInput]["ingredients"].items():
            itemIngredients[k] = v

        confirmIngredients = confirmResources(
            itemIngredients["water"],
            itemIngredients["milk"],
            itemIngredients["coffee"],
        )

        if confirmIngredients:
            print(f"Sorry there is not enough {confirmIngredients}!")
        else:

            totalRequired = MENU[machineInput]["cost"]
            totalInserted = payment()

            if totalInserted < totalRequired:
                print("Sorry that's not enough money. Money refunded.")
                continue

            if totalInserted > totalRequired:
                print(f"Here is your change of ${(totalInserted - totalRequired):.2f}")

            profit += totalRequired

            print(f"Preparing {machineInput}")
            changeResources(
                itemIngredients["water"],
                itemIngredients["milk"],
                itemIngredients["coffee"],
            )
            print(f"Here is your {machineInput}. Enjoy!")

    else:
        print("Invalid entry!")
