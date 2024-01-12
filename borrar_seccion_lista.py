"""
Función que recibe una lista de números y un número que al aparecer en la 
lista borre los elementos anteriores. EJ: [1,2,3,4,5] y num: 3 -> [3,4,5]
"""


def borra_anteriores(lista, borde):
    """
    input: lista de numeros y numero del borde
    output: lista de numeros desde el borde en adelante
    """
    try:
        return lista[lista.index(borde):]
    except ValueError:
        return lista


print(borra_anteriores([1, 2, 3, 4, 5], 3))
