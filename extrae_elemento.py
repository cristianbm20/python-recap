"""
Funcion que devuelve una tupla de tres elementos,
el primero, el tercero y el segundo por el final.
"""


def easy_unpack(elements: tuple) -> tuple:
    """
    input: tupla de tres elementos (tuple)
    output: tupla de tres elementos (tuple)
    """
    lista = list(elements)
    lista_invertida = lista[::-1]
    return lista[0], lista[2], lista_invertida[1]


print(easy_unpack((1, 5, 3, 9)))
