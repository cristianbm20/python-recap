"""
Funcion que suma los elementos de indice par de un 
array dado. El resultado de la suma lo multiplica por
el ultimo elemento.
"""


def checkio(array: list) -> int:
    """
    input: array (list)
    output: resultado (int)
    """
    pares = []
    if len(array) > 0 and len(array) <= 20:
        for i, enum in enumerate(array):
            if i == 0 or (i % 2) == 0:
                pares.append(enum)
        return sum(pares) * array[len(array)-1]
    return 0


print(checkio([1, 4, 6, 10, 4]))
