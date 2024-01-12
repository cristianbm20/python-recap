"""
Funcion que devuelve el resultado de elevar 
por n el elemento de indice n de list. 
"""


def index_power(array: list, n: int) -> int:
    """
    input: array (list), n (int)
    output: array[n] ** n (int)
    """
    if n > len(array) - 1:
        return -1
    return array[n] ** n


print(index_power([1, 2, 3, 4], 2))
print(index_power([1, 3, 10, 100], 3))
print(index_power([1, 2], 3))
