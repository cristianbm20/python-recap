"""
Funcion que mueve el primer elemento de una lista a la ultima posicion.
"""


def mueve_primero(lista):
    """
    input: lista (list)
    output: lista (list)
    """
    if len(lista) > 1:
        primero = lista[0]
        lista.append(primero)
        lista.pop(0)
        return lista
    return lista


my_list = [1, 2, 3, 4, 5]
print(mueve_primero(my_list))

# Otras soluciones


# def mueve_primero1(list):
#     if list:  # Si la lista es una lista (tiene 2 o mas elementos)
#         # .pop() borra y devuelve el elemento borrado que a su vez se añade con .append()
#         list.append(list.pop(0))
#     return list


# def mueve_primero2(list):
#     return list[1:] + list[:1]


# print(mueve_primero1([1, 2, 3, "hola"]))
# print(mueve_primero2(["primero", 2, 3]))
