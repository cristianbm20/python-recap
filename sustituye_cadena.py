"""
Funcion que une strings y reemplaza "right" por "left"
"""


def left_join(phrases: tuple) -> str:
    """
    input: phrases (tuple)
    output: string (str)
    """
    lista = ",".join(phrases)
    string = str(lista)
    print(string)
    if "right" in string:
        string = string.replace("right", "left")
    return string


print(left_join(("left", "right", "right")))
