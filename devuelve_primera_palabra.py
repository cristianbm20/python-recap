"""
Funcion que devuelve la primera palabra de un string
dado.
"""


def first_word(text: str) -> str:
    """
        input: text (str)
        output: primera palabra (str)
    """
    if "." in text or "," in text:
        text = text.replace(".", " ")
        text = text.replace(",", " ")
    lista = text.split(" ")
    contador = 0
    while not lista[contador].isalpha():
        if "'" in lista[contador]:
            return lista[contador]
        contador += 1
    return lista[contador]


print(first_word("Hello.World"))
