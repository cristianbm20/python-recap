"""
Funcion que devuelve el string más frecuente de la
cadena pasada como argumento.
"""


def most_frequent(data: list) -> str:
    """
    input: lista de letras (list)
    output: (str)
    """
    return max(set(data), key=data.count)


print(most_frequent(("a", "b", "a", "a")))
