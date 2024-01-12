"""
Funcion que devuelve el número de veces que aparecen las 
palabras de una lista pasada como parametro (words) en un 
string (text).
"""


def popular_words(text: str, words: list) -> dict:
    """
    input: text (str), words (list)
    output: diccionario con las palabras de words como claves
    y el número de veces que aparecen en text como valores (dict)
    """
    text = text.lower()
    result = {}  # Diccionario
    lista = text.split()
    for i in words:
        if i in lista:
            result[i] = lista.count(i)
        else:
            result[i] = 0
    return result


print(popular_words('''When I was One I had
just begun When I was Two I was nearly new''',
                    (['i', 'was', 'three', 'near'])))
