"""
Funcion que devuelve el articulo o articulos más 
caros de una lista de articulos pasada como argumento.
La cantidad de elementos es el argumento limit.
"""


def bigger_price(limit: int, data: list) -> list:
    """
    input: limit (int), data (list)
    output: lista con los articulos mas caros (list)
    """
    # Ordena los diccionarios por precio de menor a mayor.
    ordenados = sorted(data, key=lambda x: x['price'])
    # Los ordena de mayor a menor
    ordenados = ordenados[::-1]
    # Array donde almacenaremos los elementos con mayor precio.
    resultado = []
    for i in range(0, limit):
        resultado.append(ordenados[i])
    return resultado


print(bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]))
