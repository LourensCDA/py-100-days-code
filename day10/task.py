def formatName(fname: str, surname: str) -> str:
    """
    Docstring for formatName

    :param fname: Description for param 1
    :type fname: str
    :param surname: Description for param 2
    :type surname: str
    :return: Description for output
    :rtype: str
    """
    return (f"{fname} {surname}").title()


print(formatName("lourens", "bitha"))
