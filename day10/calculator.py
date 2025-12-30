from art import logo

print(logo)


def add(n1, n2):
    """
    Adds two numbers and returns results

    :param n1: Description
    :param n2: Description
    """
    return n1 + n2


def minus(n1, n2):
    """
    Substracts second number from first

    :param n1: Description
    :param n2: Description
    """
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# very handy to control operation selection
operations = {"+": add, "-": minus, "*": multiply, "/": divide}

result = 0
storeRes = "n"

while storeRes != "c":
    firstNumber = result
    if storeRes == "n":
        result = 0
        firstNumber = float(input("Enter first number: "))
    operation = input("+\n-\n*\n/\nEnter operation: ")
    secondNumber = float(input("Enter second number: "))

    result = operations[operation](firstNumber, secondNumber)

    print(f"Result for {firstNumber} {operation} {secondNumber} = {result}")
    storeRes = input(
        "Press y if you want to use result again or n for new calculation or c to stop"
    )
