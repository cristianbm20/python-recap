"""
Funcion que recibe una lista de booleanos 
y devuelve el más frecuente. En caso de empate
o lista vacia devuelve False.
"""


def is_majority(items: list) -> bool:
    """
    input: lista de booleanos
    output: booleano
    """
    if len(items) < 1:
        return False
    else:
        return max(sorted(items), key=items.count)


print(is_majority([True, True, False, True, False]))
print(is_majority([True, True, False, False]))
print(is_majority([False]))
print(is_majority([]))
