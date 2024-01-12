"""
Funcion que devuelva la parte de una cadena comprendida
entre los dos caracteres que se le pasan como argumento.
"""


def between_markers(text: str, begin: str, end: str) -> str:
    """
    input: cadena de texto, marca inicial y marca final
    output: cadena de texto entre marcas
    """
    start = 0
    final = 0
    for i, char in enumerate(text):
        if char == begin:
            start = i + 1
        if char == end:
            final = i
    return text[start:final]


print(between_markers("Salud<os viajeros>", "<", ">"))
