"""
Funcion que devuelve una lista con los elementos repetidos
de la lista pasada como parametro.
"""


def checkio(data: list) -> list:
    """
    input: data (list)
    output: lista con los elementos repetidos (list)
    """
    elements = set(data)
    elements = list(elements)
    for elem in elements:
        if data.count(elem) == 1:
            data.pop(data.index(elem))
    return data


print(checkio([1, 2, 3, 1, 3]))
