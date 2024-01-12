"""
Funcion que ordena una tupla por valor absoluto de 
sus elementos en orden ascendente.
"""


def checkio(values: list) -> list:
    """
    input: values (list)
    output: lista ordenada por valor absoluto (list)
    """
    return sorted(values, key=lambda x: abs(x) * len(values) - values.index(x))


print(checkio([-10, 4, 3, -1]))
