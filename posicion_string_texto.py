"""
Funcion que devuelva la posicion [fila en la que empieza,
columna en la que empieza,fila en la que termina,
columna en la que termina]. 
"""


def checkio(text, word):
    """
    input: text (str), word (str)
    output: posicion de la palabra en el texto (list)
    """
    if word in text:
        return True
    return False


print(checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ofapples"))
