"""
Funcion que devuelva True o False en funcion de 
si todos los elementos de una lista pasada son 
iguales o no.
"""

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    """
    input: elements (List[Any])
    output: True or False (bool)
    """
    if len(elements) == 0:
        return True
    return (elements.count(elements[0]) == len(elements))


print(all_the_same([1, 1, 1, 1]))
print(all_the_same([1, 2, 1, 1]))
print(all_the_same([1]))
print(all_the_same([]))
