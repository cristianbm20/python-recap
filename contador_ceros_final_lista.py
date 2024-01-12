"""
Contador de ceros a la derecha de un número.
"""


def ceros_finales(num):
    """
    input: numero (str)
    output: cantidad de ceros a la derecha (int)
    """
    return len(num) - len(num.rstrip("0"))


print(ceros_finales("1045002000"))
