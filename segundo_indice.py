"""
Funcion que devuelve la posicion(indice) que ocupa
la segunda ocurrencia de symbol en text.
"""


def second_index(text: str, symbol: str) -> int:
    """
    input: text (str), symbol (str)
    output: indice (int)
    """
    indice = 0
    if text.count(symbol) >= 2:
        indice = text.index(symbol)
        text = text.replace(text[indice], ".", 1)
        indice = text.index(symbol)
        return indice
    return None


print(second_index("hola que tal", "a"))
