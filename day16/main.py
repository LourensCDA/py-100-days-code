from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machineState = "on"

menuOptions = Menu()
machine = CoffeeMaker()
account = MoneyMachine()

while machineState == "on":

    machineInput = input(
        f"☕ What would you like to drink? {menuOptions.get_items()} "
    ).lower()

    if machineInput == "off":
        machineState = machineInput
        print("Machine is turning off")

    elif machineInput == "report":
        machine.report()
        account.report()
    else:
        order = menuOptions.find_drink(machineInput)

        if not order:
            continue

        if machine.is_resource_sufficient(order):
            if account.make_payment(order.cost):
                machine.make_coffee(order)
