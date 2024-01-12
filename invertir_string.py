"""
Funcion que invierta unicamente el orden de 
las letras de una cadena pasada como argumento
"""


def backward_string_by_word(text: str) -> str:
    """
    input: text (str)
    output: text (str)
    """
    lista = text.split(" ")
    for i, elem in enumerate(lista):
        lista[i] = elem[::-1]
    return " ".join(lista)


print(backward_string_by_word("hello   world"))  # olleh   dlrow
