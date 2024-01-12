"""
Funcion que recibe una lista y devuelve una 
tupla con dos elementos, la suma de todos los 
elementos numericos y la concatenacion de todos
los strings.
"""

from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    """
    input: items (list)
    output: tupla (str, int)
    """
    num = []
    strings = []
    for i in items:
        if isinstance(i, str):
            strings.append(i)
        else:
            num.append(i)
    num = sum(num)
    strings = "".join(strings)
    return [strings, num]


print(sum_by_types(['size', 12, 'in', 45, 0]))
print(sum_by_types([]))
