"""
Funcion que devuelve la letra mas frecuente
del string pasado.
"""


def checkio(text: str) -> str:
    """
    input: text (str)
    output: letra mas frecuente (str)
    """
    return max(sorted([i for i in text.lower() if i.isalpha()]), key=text.count)


print(checkio("ebbanab"))
