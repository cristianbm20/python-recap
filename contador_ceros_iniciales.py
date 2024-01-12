"""
Contador de ceros a la izquierda de un número.
"""


def ceros_iniciales(num):
    """
    input: numero (str)
    output: cantidad de ceros a la izquierda (int)
    """
    return len(num) - len(num.lstrip("0"))


print(ceros_iniciales("000120"))
