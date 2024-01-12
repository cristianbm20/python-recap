"""
Funcion que divida una lista en dos. 
Ej: [1,2,3,4,5,6] -> [1,2,3] [4,5,6]
Si la lista es impar la primera mitad tendrá
un elemento mas que la segunda. Si la lista
esta vacia devolvera dos listas vacias.
"""


def split_list(items: list) -> list:
    """
    input: items (list)
    output: lista con dos listas (list)
    """
    middle = int(len(items)/2)
    new_items = []
    if len(items) % 2 != 0:
        middle += 1
    new_items.append(items[:middle])
    new_items.append(items[middle:])
    return new_items


print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([]))
