"""
Funcion que devuelve el elemento de un set más cercano al 
entero dado
"""
import bisect


def nearest_value(values: set, one: int) -> int:
    """
    input: values (set), one (int)
    output: elemento más cercano a one (int)
    """
    lista = list(values)
    lista.sort()
    pos = bisect.bisect_left(lista, one)
    if pos == 0:
        return lista[0]
    if pos == len(lista):
        return lista[-1]
    before = lista[pos - 1]
    after = lista[pos]
    if after - one < one - before:
        return after
    return before


print(nearest_value({4, 7, 9, 11, 12, 3}, 10))
